import re
from dateutil.parser import parse
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
from .content import YoutubeContent


class Video(YoutubeContent):
    """
    Represents a YouTube video, encapsulating its unique identifier and core attributes. 
    Functionality to extract static video properties, statisitcs and transcript.
    """
    SHORTS_MAX_LENGTH = 60
    
    def __init__(self, video_id:str) -> None:
        super().__init__()
        self.video_id = video_id
      
        self._video_name = None 
        self._video_length = None 
        self._channel_id = None

    def __repr__(self):
        return f"Video(video_id={self.video_id})"

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.video_id == other.video_id
        return False

    def __hash__(self):
        return hash(self.video_id)
    
    def __len__(self):
        """Returns the video's length in seconds."""
        if self._video_length is None:
            self._video_length = self.get_video_properties()['length']
        return self._video_length

    @property
    def video_name(self):
        """
        Name of the video. Lazily loaded upon first access.
        """
        if self._video_name is None:
            self._video_name = self.get_video_properties()['video_name']
        return self._video_name
    
    @property
    def channel_id(self):
        """
        ID of the channel the video belongs to. Lazily loaded upon first access.
        """
        if self._channel_id is None:
            self._channel_id= self.get_video_properties()['channel_id']
        return self._channel_id
    
    def get_response(self, video_id: str, part: str):
        return self.youtube.videos().list(
            part=part,
            id=video_id
        ).execute()
    
    def get_video_properties(self) -> dict:
        """
        Fetch and return detailed properties of the video, including its name, channel, 
        publication date, length, type, license, etc.
        """
        response = self.get_response(self.video_id, 'contentDetails, snippet, status')

        # processing video length
        duration = response['items'][0].get('contentDetails', {}).get('duration', 'Not Found')
        if duration != 'Not Found':
            video_length = self._convert_time_to_seconds(duration)
        else:
            video_length = 0
        
        # processing other response parts
        snippet = response['items'][0]['snippet']
        status = response['items'][0]['status']

        video_stats = {
            "video_id": self.video_id,
            "video_name": snippet.get('title', 'Not Found'),
            "channel_id": snippet.get('channelId', 'Not Found'),
            "channel_name": snippet.get('channelTitle', 'Not Found'),
            "category_id": snippet.get('categoryId', 'Not Found'),
            "published_at": self._parse_date(snippet.get('publishedAt', 'Not Found')),
            "length": video_length,
            "type": ("shorts" if video_length <= self.SHORTS_MAX_LENGTH else "video"),
            "license": "Standard License" if status.get('license', 'Not Found') == 'youtube' else "Creative Commons",
            "made_for_kids": status.get('madeForKids', 'Not Found'),
            "user_tags": snippet.get('tags', []),
            "description": snippet.get('description', 'Not Found'),
        }
        return video_stats
    
    def get_video_statistics(self) -> dict:
        """
        Fetch and return statistics of the video, including views, likes, and comments.
        """
        response = self.get_response(self.video_id, 'statistics, contentDetails')
        
        video_stats = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "video_id": self.video_id,
            "views": response['items'][0]['statistics']['viewCount'],
            "likes": response['items'][0]['statistics']['likeCount'],
            "comments": response['items'][0]['statistics'].get('commentCount', 0),
        }
        return video_stats
    
    def get_video_data(self) -> dict:
        properties = self.get_video_properties()
        statistics = self.get_video_statistics()
        return properties | statistics

    def get_video_transcript(self):
        """
        Fetch and return the transcript of the video in a consolidated string format.
        """
        id = self.video_id[:11]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(id)
            full_transcript = {"transcript": " ".join([part['text'] for part in transcript])}

        except TranscriptsDisabled:
            full_transcript = {"transcript": "transcript-disabled"}

        except NoTranscriptFound:
            full_transcript = {"transcript": "transcript-not-found"}

        except VideoUnavailable:
            full_transcript = {"transcript": "transcript-unavailable"}

        return full_transcript  

    @staticmethod
    def _convert_time_to_seconds(time_string: str) -> int:
        """
        Convert a given duration format (used by YouTube) to total seconds.
        """
        pattern = r'PT((\d+)H)?((\d+)M)?((\d+)S)?'
        match = re.match(pattern, time_string)

        hours = int(match.group(2)) if match.group(2) else 0
        minutes = int(match.group(4)) if match.group(4) else 0
        seconds = int(match.group(6)) if match.group(6) else 0

        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds

    @staticmethod
    def _parse_date(date_string: str) -> str:
        """
        Convert a given date string to standard ISO format.
        """
        return parse(date_string).date().isoformat()
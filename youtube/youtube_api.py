import os
from typing import Literal
from googleapiclient.discovery import build

class YouTubeAPI:
    """
    A class to interact with the YouTube Data API v3, providing methods to fetch video details, 
    channel details, search results, and playlist items.
    """
    def __init__(self):
        self.youtube = self.build_youtube_object()

    def build_youtube_object(self):
        """Builds and returns the YouTube API service object."""
        api_key = os.environ.get('YOUTUBE_API_KEY')
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY environment variable is not set.")
        
        return build('youtube', 'v3', developerKey=api_key)

    def get_video_response(self, video_id: str, part: str):
        return self.youtube.videos().list(
            part=part,
            id=video_id
        ).execute()

    def get_channel_response(self, channel_id: str, part: str):
        return self.youtube.channels().list(
            part=part,
            id=channel_id
        ).execute()
    
    def get_search_response(
            self, 
            key: str, 
            part: str,
            type: Literal["video", "channel", "playlist", "movie"],
            order_by: Literal["viewCount", "relevance", "date"],
            max_results: int,
            published_after = None
            ):
        
        return self.youtube.search().list(
                q=key,
                type=type,
                order=order_by,
                publishedAfter=published_after,
                part=part,
                maxResults=max_results
            ).execute()

    def get_playlist_response(
            self,
            playlist_id: str,
            part: str,
            max_results: int = 50,
            page_token = None
        ):

        return self.youtube.playlistItems().list(
                part=part,
                playlistId=playlist_id,
                maxResults=max_results,
                pageToken=page_token
            ).execute()
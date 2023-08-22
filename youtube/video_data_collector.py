from typing import Optional
from tqdm import tqdm
from .video import Video
from .playlist import Playlist
from .channel import Channel


class VideoDataCollector:
    """
    YoutubeDataCollector class is responsibe for gathering data via custom interface for
    YouTube api. It provides two methods for data collection: collect_data_from_channel and collect_data_from_videos.
    """
    def __init__(self, channel_ids: Optional[list[str]] = None, 
                 video_ids: Optional[list[str]] = None, 
                 playlist_ids: Optional[list[str]] = None):
        
        self.channel_ids = channel_ids or []
        self.video_ids = video_ids or []
        self.playlist_ids = playlist_ids or []

    def collect_data_from_channels(self, max_videos: int = 50) -> list[dict]:
        """
        Collects data from provieded channel ids. Designed for static data, method combines video properties and 
        video transcript. Results are saved in dictionary format.
        """
        all_video_data = []

        if not len(self.channel_ids):
            raise ValueError("Methods requires channel_ids to collect data.")

        for channel_id in tqdm(self.channel_ids, desc="Processing videos from channel ids"):
            channel = Channel(channel_id)
            channel_videos = channel.get_channel_videos(max_videos)

            for video in channel_videos:
                try:
                    video_data = video.get_video_properties() | video.get_video_transcript()
                    all_video_data.append(video_data)

                # youtube transcript api sometimes returns connection errors. 
                # After they occur, Video.get_transcript() method raises ValueError. 
                # Becouse these are rare, I chose to skip when found.
                except ValueError:
                    continue

        return all_video_data

    def collect_data_from_videos(self) -> list:
        """
        Collects data from video ids. Designed for dynamic data (data that is changing over time).
        Results are saved in dictionary format.
        """
        all_video_data = []

        if not len(self.video_ids):
            raise ValueError("Methods requires video_ids to collect data.")

        for video_id in tqdm(self.video_ids, desc="Processing videos from video ids"):
            video = Video(video_id)
            video_data = video.get_video_stats()
            all_video_data.append(video_data)

        return all_video_data
    
    def collect_data_from_playlists(self, max_videos: int = 50) -> list:
        """
        """
        all_video_data = []

        if not len(self.playlist_ids):
            raise ValueError("Methods requires video_ids to collect data.")
        
        if max_videos > 50:
            raise NotImplementedError("Fetching data from more then 50 videos per playlist is currently not supported.")
        
        for playlist_id in tqdm(self.playlist_ids, desc="Processing videos from playlist ids"):
            playlist = Playlist(playlist_id)
            playlist_videos = playlist.get_playlist_videos(max_results=max_videos)

            for video in playlist_videos:
                video_data = video[0].get_video_properties() | video[0].get_video_transcript()
                all_video_data.append(video_data)

        return all_video_data

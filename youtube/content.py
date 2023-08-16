import os
from abc import ABC, abstractmethod
from googleapiclient.discovery import build


class YoutubeContent(ABC):

    def __init__(self):        
        self.youtube = self.build_youtube_object()
        self.response_data = None

    def build_youtube_object(self):
        """Builds and returns the YouTube API service object."""
        api_key = os.environ.get('YOUTUBE_API_KEY')
        if not api_key:
            raise ValueError("YOUTUBE_API_KEY environment variable is not set.")
        
        return build('youtube', 'v3', developerKey=self.api_key)

    @abstractmethod
    def get_response(self, **kwargs):
        """
        Abstract method to be overridden by subclasses.
        Fetches and stores content from the YouTube API.
        """
        pass




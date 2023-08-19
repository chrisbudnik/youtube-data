## YouTube Module Architecture

### Overview:
The YouTube module is a comprehensive tool built around the YouTube API, designed to extract and process data seamlessly. This guide aims to provide insights into its architectural design, breaking down the logic and functionalities of its components.

### Design Architecture:

#### Core:
At the heart of this module lies the `YoutubeContent` class, an abstract base class which serves as the foundation for the major components: `Video`, `Channel`, `Playlist`, and `YoutubeSearch`. It's responsible for establishing the YouTube API connection, ensuring that all subclasses have access to it.

```python
class YoutubeContent(ABC):

    # Constructor to initialize the YouTube API connection
    def __init__(self):        
        self.youtube = self.build_youtube_object()

    # Method to create and return the YouTube API service object
    def build_youtube_object(self):
        ...
    # Abstract method to be overridden by subclasses for fetching content
    @abstractmethod
    def get_response(self, **kwargs):
        pass
```

#### Data Structure Hierarchy:
1. **Video**: This is the smallest and most granular data structure. It contains methods that allow extraction of static properties, dynamic statistics, and video transcripts.
```python
class Video:
    ...

    def get_video_properties(self):
        """
        Extracts details such as "video_id", "video_name", "channel_id", 
        "channel_name", "category_id", "published_at", "video_length", 
        "type", "license", "made_for_kids", "user_tags", and "description".
        """
        pass

    def get_video_statistics(self):
        """
        Provides statistics like ["date", "video_id", "views", "likes", "comments"].
        """
        pass

    def get_video_transcript(self):
        """Extracts video transcript."""
        pass
```
2. **Playlist**: Represents a collection of videos. It has a primary function of extracting all videos that are part of it. This is achived with `get_playlist_videos` method that gathers all correspodning `Video` in a list format.
```python
class Playlist:
    ...

    def get_playlist_videos(self):
        """Gathers all corresponding Video elements in a list format."""
        pass
```
3. **Channel**: The highest level in the data hierarchy. It encompasses both videos and playlists. It offers functionalities such as finding a playlist by its name and extracting all videos from the "uploads" playlist.
```python
class Channel:
    ...
    
    def get_channel_videos(self):
        """Determines the uploads playlist ID and returns a list of Video elements."""
        pass

    def get_playlist_id(self, name):
        """Finds the ID of a playlist based on the provided name."""
        pass
```

The hierarchy visualizes as: **Channel** > **Playlist** > **Video**. This encapsulates the real-world relationship of YouTube entities.

#### **YoutubeSearch**:
Built atop `YoutubeContent`, this class offers search functionalities. Its prowess is showcased in methods such as `collect_exact_terms`, which finds channel IDs based on their names, and `best_ranking_channels`, which ranks channels based on video view counts and selected keywords.

#### **VideoDataCollector**:
This interface simplifies the data collection process. It operates with two main methods:
1. `get_data_from_channels`: Extracts video data using a list of channel IDs.
2. `get_data_from_videos`: Retrieves video data using a list of video IDs.

For conveniance `VideoDataCollector` can serve both functionalities at the same time, since it allows provision of both channel IDs and video IDs.

### Final Thoughts:
The architectural design of the YouTube module adheres to the principles of modularity and hierarchy, mirroring the YouTube data model for intuitive understanding and easy scalability. Whether you are fetching data for a single video, aggregating content from a playlist, or diving deep into channel analytics, this module is crafted to ensure efficiency and ease of use.



```python
class Channel:

    def get_channel_videos(self):
        """Determines the uploads playlist ID and returns a list of Video elements."""
        pass

    def get_playlist_id(self, name):
        """Finds the ID of a playlist based on the provided name."""
        pass
```


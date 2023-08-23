# Tutorials - Youtube Data Toolset

Welcome to the tutorials section of the Youtube Data Toolset. This section is tailored to guide you through the comprehensive functionalities of the repository, ensuring you make the most out of the YouTube data collection and analysis.

## 📚 Tutorials Index:

### 1. **Channel Discovery** [`channel-discovery.py`]
- Read search terms from a `.txt` file.
- Utilize `YoutubeSearch` to find top-ranking channels.
- Extract essential channel information, such as:
  - Channel ID
  - Channel Name
  - Uploads Playlist ID
  - Subscriber Count
- Insert the extracted data into a BigQuery table using the CSV format.

### 2. **Find Channel IDs** [`find-channel-ids.py`]
- Extract search terms from a `.txt` file.
- Employ the `search_exact_terms()` method under the `YoutubeSearch` class to pinpoint IDs based on specific channel names.
- Save the results into a CSV file.

### 3. **Collect Video Properties** [`collect-video-properties.py`]
- Read a CSV file containing channel IDs.
- Delve deep with `VideoDataCollector` and harness the power of the `collect_data_from_channels()` method:
  - Collect video property data from the latest n videos of each channel.
- Export this data to a CSV file.

### 4. **Collect Video Data** [`collect-video-stats.py`]
- Read a CSV file containing channel IDs.
- Utilize Channel method `get_channel_videos` and 
- Video methods used: `get_video_properties` and `get_video_statistics`
  - Extract video statistics pertinent to the current date.
- While reading channels, simultaneously save to respective csv files

## 🚀 Getting Started:
1. Navigate to the desired tutorial file.
2. Ensure all dependencies are installed and credentials are set up (use environment variables).
3. Follow along, modify the scripts as needed, and deepen your understanding of data collection from YouTube.

Thank you for exploring the Youtube Data Toolset tutorials. Happy data collecting!
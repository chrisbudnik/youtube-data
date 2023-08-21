# **Youtube Data**

Welcome to the Youtube-Data repository. Dive into an efficient suite designed for extracting and analyzing data from YouTube using the YT API v3. Built with Python, this repository provides comprehensive modules to get the most out of YouTube data.

## 📌 Features:
- **`Video`**: Extract both static properties and dynamic stats.
- **`Playlist`**: Fetch video IDs from any given playlist.
- **`Channel`**: Retrieve all video IDs associated with a channel.
- **`YoutubeSearch`**: A dedicated class to find channels or inspect video IDs.
- **`VideoDataCollector`**: A class to fetch video data based on video or channel IDs.
- **`Trending`** Fetch video IDs from country's trending page - *in progess*.

## 📁 Directory Structure:
### 1. `youtube`
- This directory houses core functionality and classes associated with YouTube data extraction and manipulation:
  - `Video`, `Playlist`, and `Channel` classes for various data extraction tasks.
  - `YoutubeSearch` class for enhanced search functionality.
  - `VideoDataCollector` interface for a cohesive data collection experience.

### 2. `examples`
- Provides instructive code samples for various functionalities including:
  - Channel discovery.
  - Finding channel IDs (exact keyword search).
  - Extracting video properties and statistics.

## 🚀 Setup

To get started with the Youtube-Data repository and take full advantage of its powerful features, follow the steps below:

1. **Environment Setup**:
   - Clone the repository to your local machine.
   - Navigate to the root directory of the project.
   - Install the required packages using:
     ```bash
     pip install -r requirements.txt
     ```

2. **API Key Configuration**:
   - Before utilizing the modules, you need to have a YouTube API v3 key. Generate one using the [Google Cloud Platform Console](https://console.cloud.google.com/).
   - Once you have the key, set up an environment variable named `YOUTUBE_API_KEY`. Depending on your operating system, you can set it as:
     - For Linux/MacOS:
       ```bash
       export YOUTUBE_API_KEY="YOUR_API_KEY"
       ```
     - For Windows:
       ```cmd
       set YOUTUBE_API_KEY="YOUR_API_KEY"
       ```

3. **Install as a Package**:
   - If you want to install the repository as a Python package for easier import in your projects, run:
     ```bash
     python setup.py install
     ```

Now you're all set! Dive into the `examples` directory to see some practical implementations and get a feel for how to leverage the provided classes and methods.
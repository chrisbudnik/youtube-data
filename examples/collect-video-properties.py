# Tutorial Outline
# 1. Retrive channel ids from csv file (channel-list-custom.csv)
# 2. Collect video properties with `VideoDataCollector` 
# 3. Save results into csv file (get data from latest 25 videos)

import sys
sys.path.append('/Users/chrisbudnik/Desktop/Projects/youtube-research')

import csv
from youtube import VideoDataCollector


# Save channel ids in list format from csv file
channel_ids = []
with open('/Users/chrisbudnik/Desktop/Projects/youtube-data/examples/data/channel-search-business-v2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        channel_ids.append(row['channel_id'])

# Create an instance of VideoDataCollector
collector = VideoDataCollector(channel_ids=channel_ids)

# Collect video data from channel ids
data_from_channels = collector.collect_data_from_channels(max_videos=25)

with open('/Users/chrisbudnik/Desktop/Projects/youtube-data/examples/data/video-properties-business.csv', 'w') as file:
    writer = csv.writer(file)
    header = ["video_id", "video_name", "channel_id", "channel_name",
              "category_id", "published_at", "video_length", "type",
              "license", "made_for_kids", "user_tags", "description",
              "transcript"]
    
    writer.writerow(header)

    for video in data_from_channels:
        properties = list(video.values())
        writer.writerow(properties)

print(f"Successfuly saved data from {len(data_from_channels)} video.")

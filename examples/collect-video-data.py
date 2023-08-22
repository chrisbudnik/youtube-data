import sys
sys.path.append('/Users/chrisbudnik/Desktop/Projects/youtube-data')

import csv
import time

from tqdm import tqdm
from youtube import Channel

PATH_TO_CHANNEL_DATA = "examples/data/channel-search-business-v2.csv"
PATH_TO_PROPERTIES = "examples/data/video-properties-business-v2.csv"
PATH_TO_STATS = "examples/data/video-stats-business-v2.csv"

p_errors = 0
s_errors = 0
n_videos = 0

start_time = time.time()

with open(PATH_TO_CHANNEL_DATA, 'r') as channelid_csv, open(PATH_TO_PROPERTIES, "w") as properties_csv, open(PATH_TO_STATS, "w") as stats_csv:
    # reader
    reader = csv.DictReader(channelid_csv)

    # properties writer
    pwriter = csv.writer(properties_csv)
    pheader = ["video_id", "video_name", "channel_id", "channel_name",
               "category_id", "published_at", "video_length", "type",
               "license", "made_for_kids", "user_tags", "description",
               "transcript"]
    pwriter.writerow(pheader)

    # stats writer 
    swriter = csv.writer(stats_csv)
    sheader = ["date", "video_id", "views", "likes", "comments"]
    swriter.writerow(sheader)

    # iteration
    for row in tqdm(reader, desc="Processing channels..."):
        # get channel videos
        channel = Channel(channel_id=row['channel_id'])
        channel_videos = channel.get_channel_videos(max_results=25)

        # iterate over channel videos
        for video in channel_videos:
            n_videos += 1

            try:
                # extract properties
                properties = video.get_video_properties()
                pwriter.writerow(list(properties.values()))
            except Exception:
                p_errors += 1

            try: 
                # extract stats
                stats = video.get_video_statistics()
                swriter.writerow(list(stats.values()))
            except Exception:
                s_errors += 1

end_time = time.time()

elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = elapsed_time % 60

print(f"Script executed in {minutes} minutes and {seconds:.2f} seconds")
print(f"Videos retrived: {n_videos}")
print(f"Stats extraction errors: {s_errors}")
print(f"Property extraction errors: {p_errors}")



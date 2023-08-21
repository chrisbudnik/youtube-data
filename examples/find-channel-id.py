import sys
sys.path.append('/Users/chrisbudnik/Desktop/Projects/youtube-research')

import csv
from youtube import YouTubeSearch


# Retrive custom list of channel names to find their IDs (from .txt file)
with open('/Users/chrisbudnik/Desktop/Projects/youtube-data/examples/data/channels-search-ids.txt', 'r') as file:
    exact_search_terms = [line.strip() for line in file]

# Create an instance of YoutubeSearch
search = YouTubeSearch(keywords=exact_search_terms)
results = search.collect_exact_terms()

# Save results to csv file 
with open('/Users/chrisbudnik/Desktop/Projects/youtube-data/examples/data/channel-search-from-exact.csv', 'w') as file:
    writer = csv.writer(file)
    header = ["channel_id", "channel_name", "uploads_playlist_id", "subscriber_count"]
    writer.writerow(header)

    for channel in results:
        # use `info()` method to access main channel properties
        channel_info = list(channel.info())
        writer.writerow(channel_info)

# Warning is printed if some keywords were not found
print(f"Successfuly saved {len(results)}")
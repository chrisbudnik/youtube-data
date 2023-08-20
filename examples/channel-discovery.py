import sys
import csv
from tqdm import tqdm

# Appending folder with youtube module 
sys.path.append('/Users/chrisbudnik/Desktop/Projects/youtube-data')
from youtube import YouTubeSearch

# Parsing search terms saved in .txt file.
with open('examples/data/keywords-business.txt', 'r') as file:
    search_terms = [line.strip() for line in file]

# Crating an instance of YoutubeSearch
search = YouTubeSearch(keywords=search_terms)

# Max results is set to 10 (youtube api limit is 50)
results = search.collect_best_ranking_channels(max_results = 50, 
                                               timeframe=180,
                                               order_by="relevance", 
                                               only_unique=True)

# Saving results into csv file
with open('examples/data/channel-search-business-v2.csv', 'w') as file:
    writer = csv.writer(file)
    header = ["channel_id", "channel_name", "uploads_playlist_id", "subscriber_count"]
    writer.writerow(header)

    for channel in tqdm(results, desc="Saving channel info ..."):
        channel_info = list(channel.info())
        writer.writerow(channel_info)

print(f"Successfuly saved {len(results)} channels.")

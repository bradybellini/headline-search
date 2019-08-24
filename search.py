import feedparser
from feeds import rss_feeds

# feeds = ['https://kotaku.com/rss', 'https://www.pcgamer.com/rss']
for feed in rss_feeds:
    f = feedparser.parse(feed)
    [print(entry['title']) for entry in f.entries if 'Games' in entry['title']]
# print(f.entries[0]['title'])
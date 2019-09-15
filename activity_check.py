import feedparser
import json
import time
import requests

#check if match or etag for feed or pass if neither
#Curretly put on hold. Less than a third of the feeds have etag or last-modified built into feed. Need to check actualy cache headers
#for a better solution. I wont be updating feeds enough for this to be too big of a problem, but the bandwidth could add up in the long run.
#The feed itself has a last updated attribute, but getting that requires donwnloading the whole feed so it defeats the purpose.
def if_change():
    with open('feeds.json', 'r') as read_file:
        f = json.load(read_file)
    for feed in f['gaming']:
        f = feedparser.parse(feed['feed'])
        try:
            modified = f.modified if f.modified else None
            etag = f.etag if f.etag else None
            print(modified, etag)
        except:
            etag = None
            modified = None
            print(modified, etag)


if_change()
import feedparser
import json
import time
import requests

#check if match or etag for feed or pass if neither
r = requests.get('https://www.cnet.com/rss/gaming/')
print(r.headers)

def has_feed_etag():
    pass

def has_feed_mod():
    pass

def has_feed_none():
    pass
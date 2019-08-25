import feedparser
import sqlite3
import datetime
import time
from feeds import all_feeds

def main():
    for feed in all_feeds:
        f = feedparser.parse(feed)
        for entry in f.entries:
            author = entry['author'] if 'author' in entry else None
            try:
                published = time.asctime(entry.published_parsed) if 'published' in entry else None
            except:
                published = entry.published if 'published' in entry else None
            link = entry['link'] if 'link' in entry else None
            guid = entry['id'] if 'id' in entry else None
            title = entry['title'] if 'title' in entry else None
            date_added = datetime.datetime.now()
            news = sqlite3.connect('news.db')
            cursor = news.cursor()
            sql = (f"INSERT INTO headlines(title, link, author, feed, date_published, date_added, guid) VALUES(?,?,?,?,?,?,?)")
            val = (title, link, author, feed, published, date_added, guid)
            try:
                cursor.execute(sql, val)
            except:
                pass
            news.commit()
            cursor.close()
            news.close()
# print(f.entries[0]['title'])
#TODO check if link to article works if not try guid if not dont put it in database
#change date_added to be the same format as published date also change date for published to only be numbers for sorting purposes. it is not sorting right in database
#check for an id another way. Some feeds do not have a guid i.e. tech hive, pcworld feed, macworld, metacritic, sports 24
if __name__ == "__main__":
    main()
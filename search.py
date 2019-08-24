import feedparser
import sqlite3
import datetime
from feeds import rss_feeds

def main():
    for feed in rss_feeds:
        f = feedparser.parse(feed)
        for entry in f.entries:
            author = entry['author'] if 'author' in entry else None
            published = entry['published'] if 'published' in entry else None
            date_added = datetime.datetime.now()
            main = sqlite3.connect('main.db')
            cursor = main.cursor()
            sql = (f"INSERT INTO headlines(title, link, author, feed, date_published, date_added, guid) VALUES(?,?,?,?,?,?,?)")
            val = (entry['title'], entry['link'], author, feed, published, date_added, entry['id'])
            try:
                cursor.execute(sql, val)
            except:
                pass
            main.commit()
            cursor.close()
            main.close()
# print(f.entries[0]['title'])

if __name__ == "__main__":
    main()
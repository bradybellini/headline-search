import feedparser
import sqlite3
import datetime
from feeds import rss_feeds

# feeds = ['https://kotaku.com/rss', 'https://www.pcgamer.com/rss']
def main():
    for feed in rss_feeds:
        f = feedparser.parse(feed)
        for entry in f.entries:
            author = entry['author'] if 'author' in entry else None
            published = entry['published'] if 'published' in entry else None
            date_added = datetime.datetime.now()
            main = sqlite3.connect('main.db')
            cursor = main.cursor()
            cursor.execute("SELECT guid FROM headlines")
            guid_dup = cursor.fetchall()
            for guid in guid_dup:
                if entry['id'] in guid[0]:
                    pass
                else:
                    sql = (f"INSERT INTO headlines(title, link, author, feed, date_published, date_added, guid) VALUES(?,?,?,?,?,?,?)")
                    val = (entry['title'], entry['link'], author, feed, published, date_added, entry['id'])
                    cursor.execute(sql, val)
            main.commit()
            cursor.close()
            main.close()
# print(f.entries[0]['title'])

if __name__ == "__main__":
    main()
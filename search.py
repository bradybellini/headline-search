import feedparser
import sqlite3
import datetime
import time
from feeds import all_feeds






def get_entry():
    for feed in all_feeds:
        f = feedparser.parse(feed)
        for entry in f.entries:
            mandatory_elements(entry)
    return feed


def mandatory_elements(entry):
    try:
        if not 'id' in entry:
            guid = entry.link + entry.author
            parse_entry(entry, guid)
        elif not 'published' in entry:
            pass
        else:
            guid = entry.guid
            parse_entry(entry, guid)
    except:
        try:
            if not 'id' in entry or not 'published' in entry:
                pass
            else:
                guid = entry.guid
                parse_entry(entry, guid)
        except:
            pass


def parse_entry(entry, guid):
    author = entry.author if 'author' in entry else 'No author provided'
    date_published = date_format(entry)
    title = entry.title
    date_added = time.time()
    link = entry.link
    insert_data(title, link, author, date_published, date_added, guid)


def date_format(entry):
    try:
        published = time.mktime(entry.published_parsed)
        return published
    except:
        pass


def insert_data(title, link, author, date_published, date_added, guid):
    news = sqlite3.connect('news.db')
    cursor = news.cursor()
    sql = (f"INSERT INTO headlines(title, link, author, date_published, date_added, guid) VALUES(?,?,?,?,?,?)")
    val = (title, link, author, date_published, date_added, guid)
    try:
        cursor.execute(sql,val)
    except:
        print('error in instert_data')
        pass
    news.commit()
    cursor.close()
    news.close()


if __name__ == "__main__":
    get_entry()

#TODO check if link to article works if not try guid if not dont put it in database
#add all if else, try expect to handle all errors and make all data uniform so it is easier to parse in database
#check for etag and modified for rss feeds, if the feed has it, to limit bandwidth and ping to rss feed
#make functions above into class
#count occurences of certain words in a period of time to see what is trending. Might need to use nltk or something to get nound and subjects in headlines
#graph occurence vs time and take derivative to help gauge trendyness
#think about parsing summaries, descriptions for nounds for trending
#add better search for discord bot
#think about adding more tables for each category and test speeds for searching.
#add tags if they exists and category the article is in
#switch to using json doc with all feeds and site
#add source to result, i.e. kotaku.com is kotaku cnn.com is cnn


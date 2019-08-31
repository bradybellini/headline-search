import feedparser
import sqlite3
import time
import nltk
import json
from nltk.corpus import stopwords
from feeds import game_feeds


# def get_entry():
#     with open('feeds.json', 'r') as read_file:
#         f = json.load(read_file)
#     for feed in f['gaming']:
#         f = feedparser.parse(feed['feed'])
#         for entry in f.entries:
#             mandatory_elements(entry)
def get_entry():
    for feed in game_feeds:
        f = feedparser.parse(feed)
        for entry in f.entries:
            mandatory_elements(entry)

def mandatory_elements(entry):
    try:
        if not 'id' in entry:
            guid = entry.link + entry.author
            insert_data(entry=entry, guid=guid)
        elif not 'published' in entry:
            pass
        else:
            guid = entry.guid
            insert_data(entry=entry, guid=guid)
    except:
        try:
            if not 'id' in entry or not 'published' in entry:
                pass
            else:
                guid = entry.guid
                insert_data(entry=entry, guid=guid)
        except:
            pass
            print('all failed in mand')


def date_format(entry):
    try:
        published = time.mktime(entry.published_parsed)
        insert_data(date_published=published)
        print('date sucessful')
    except:
        print('error in date_format')
        pass
    print('date ran')

def get_tags(entry):
    print('tags ran')
    try:
        tags = entry.tag['term']
        insert_data(tags=tags)
        print('tags sucessful')
    except:
        stop_words = set(stopwords.words('english')) 
        all_nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(entry.title)) if pos[0] == 'N']
        tags = []
        for w in all_nouns: 
            if w.lower() not in stop_words: 
                tags.append(w) 
        tags = ', '.join(tags)
        insert_data(tags=tags)
        print('error in tags')




def insert_data(**kwargs):
    get_tags(kwargs.get('entry'))
    author = kwargs.get('entry').author if 'author' in kwargs.get('entry') else 'No author provided'
    game_news = sqlite3.connect('game_news.db')
    cursor = game_news.cursor()
    print(kwargs.get('tags'))
    sql = (f"INSERT INTO news(title, link, author, tags, date_published, date_added, guid) VALUES(?,?,?,?,?,?,?)")
    val = (kwargs.get('entry').title, kwargs.get('entry').link, author, kwargs.get('tags'), kwargs.get('date_published'), time.time(), kwargs.get('guid'))
    try:
        cursor.execute(sql,val)
    except:
        pass
        print('error in insert_data')
    game_news.commit()
    cursor.close()
    game_news.close()


if __name__ == "__main__":
    get_entry()

#TODO check if link to article works if not try guid if not dont put it in database
#add all if else, try expect to handle all errors and make all data uniform so it is easier to parse in database
#check for etag and modified for rss feeds, if the feed has it, to limit bandwidth and ping to rss feed
#make functions above into class
#count occurences of certain words in a period of time to see what is trending. Might need to use nltk or something to get nound and subjects in headlines
#graph occurence vs time and take derivative to help gauge trendyness
#think about parsing summaries, descriptions for nouns for trending
#add better search for discord bot
#think about adding more tables for each category and test speeds for searching.
#add source to result, i.e. kotaku.com is kotaku cnn.com is cnn


import feedparser
import sqlite3
import time
import nltk
import json
from nltk.corpus import stopwords



def get_entry():
    with open('feeds.json', 'r') as read_file:
        f = json.load(read_file)
    for feed in f['gaming']:
        f = feedparser.parse(feed['feed'])
        for entry in f.entries:
            mandatory_elements(entry)


def mandatory_elements(entry):
    try:
        if not 'id' in entry:
            guid = entry.link + entry.author
            insert_data(entry, guid)
        elif not 'published' in entry:
            pass
        else:
            guid = entry.guid
            insert_data(entry, guid)
    except:
        try:
            if not 'id' in entry or not 'published' in entry:
                pass
            else:
                guid = entry.guid
                insert_data(entry, guid)
        except:
            pass


def get_tags(entry):
    try:
        tags = entry.tag['term']
        return tags
    except:
        stop_words = set(stopwords.words('english')) 
        all_nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(entry.title)) if pos[0] == 'N']
        tags = []
        for w in all_nouns: 
            if w.lower() not in stop_words: 
                tags.append(w) 
        tags = ', '.join(tags)
        return tags


def date_format(entry):
    try:
        published = time.mktime(entry.published_parsed)
        return published
    except:
        print('get date published failed')
        pass


def insert_data(entry, guid):
    try:
        author = entry.author if 'author' in entry else 'No author provided'
    except:
        author = 'No author provided'
        print('get author failed')
    game_news = sqlite3.connect('game_news.db')
    cursor = game_news.cursor()
    sql = (f"INSERT INTO news(title, link, author, tags, date_published, date_added, guid) VALUES(?,?,?,?,?,?,?)")
    val = (entry.title, entry.link, author, get_tags(entry), date_format(entry), time.time(), guid)
    try:
        cursor.execute(sql,val)
    except:
        pass
    game_news.commit()
    cursor.close()
    game_news.close()


if __name__ == "__main__":
    get_entry()

#TODO check if link to article works if not try guid if not dont put it in database or delete
#In-progress - clean up tags when making them
#make functions above into class
#add source to result, i.e. kotaku.com is kotaku cnn.com is cnn


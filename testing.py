import feedparser
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
# game_feeds = ['https://kotaku.com/rss', 'https://www.usgamer.net/rss']
# general_feeds = ["https://twinfinite.net/feed/", "https://www.cnet.com/rss/gaming/"]
# r = requests.get('https://kotaku.com/rss')
# rr = r.headers.get('Etag')
# feed_list = [game_feeds, worldnews_feeds, usnews_feeds, technology_feeds, movies_feeds, sports_feeds, entertainment_feeds]
# feeds= {}
# feeds['gaming'] = []
# feeds['general'] = []
# feeds['technology'] = []
# feeds['politics'] = []
# feeds['movies'] = []
# feeds['sports'] = []
# feeds['entertainment'] = []

# , usnews, technology, movies, sports, entertainment
# , usnews_feeds, technology_feeds, movies_feeds, sports_feeds, entertainment_feeds
# for game in game_feeds:
#     f = feedparser.parse(game)
#     feeds['gaming'].append({
#                     'name': f.feed.title,
#                     'website_url': f.feed.link,
#                     'feed': game})
# for general in generalnews_feeds:
#     f = feedparser.parse(general)
#     feeds['general'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': general})
# for technology in technology_feeds:
#     f = feedparser.parse(technology)
#     feeds['technology'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': technology})
# for politics in politics_feeds:
#     f = feedparser.parse(politics)
#     feeds['politics'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': politics})
# for movies in movies_feeds:
#     f = feedparser.parse(movies)
#     feeds['movies'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': movies})
# for sports in sports_feeds:
#     f = feedparser.parse(sports)
#     feeds['sports'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': sports})
# for entertainment in entertainment_feeds:
#     f = feedparser.parse(entertainment)
#     feeds['entertainment'].append({
#                 'name': f.feed.title,
#                 'website_url': f.feed.link,
#                 'feed': entertainment})
# with open('feeds_2.json', 'w') as a:
#     json.dump(feeds, a)

# ff = feedparser.parse('https://www.cnet.com/rss/gaming/', modified=f.modified)
# print(ff.status)


#HOW TO OPEN JSON FILE
# with open('feeds.json', 'r') as read_file:
#     f = json.load(read_file)
# for name in f['gaming']:
#     print(name['name'])

# stop_words = set(stopwords.words('english')) 
f = feedparser.parse("https://kotaku.com/rss")
# entry_title = f.entries[2].title
# tags = f.entries[2].tags[1]['term']
# print(tags)
# word_tokens = word_tokenize(entry_title) 
# filtered_sentence = [w for w in word_tokens if not w in stop_words] 
# filtered_sentence = [] 
  
# for w in word_tokens: 
#     if w.lower() not in stop_words: 
#         filtered_sentence.append(w) 
  

# all_nouns = [word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(entry_title)) if pos[0] == 'N']
# # print(nouns)
# nouns = []
# for w in all_nouns: 
#     if w.lower() not in stop_words: 
#         nouns.append(w) 
# print(', '.join(nouns))
def myFun(arg1, **kwargs):  
    print(kwargs.get('title').title)
    # for key, value in kwargs.items(): 
    #     print ((key)) 
  
# Driver code 
myFun("Hi", title=f.entries[2]) 
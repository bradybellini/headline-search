import datetime
import sqlite3
import re

#On hold- Need to figure out better way to get tags in a list that are clean and not in tuples
#look into not using sqlite for tags and use another option like csv and pandas to manipulate data
#Find out how to export one column to csv and def use pandas

def pull_tags():
    game_news = sqlite3.connect('game_news.db')
    cursor = game_news.cursor()
    cursor.execute(f"SELECT title FROM news")
    result = cursor.fetchone()
    cursor.close()
    game_news.close()
    print(result)
def is_trending():
    pass



if __name__ == "__main__":
    pull_tags()

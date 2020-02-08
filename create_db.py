import sqlite3
from sqlite3 import Error
 
 
def create(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute("""CREATE TABLE all_headlines (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE gaming (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE sports (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE general (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE technology (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE politics (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")

        c.execute("""CREATE TABLE entertainment (
    title TEXT,
    link TEXT,
    author TEXT DEFAULT 'None',
    date_published TEXT,
    date_added INTEGER,
    guid TEXT NOT NULL UNIQUE)""")
        conn.commit()
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create(r"news.db")

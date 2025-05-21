import sqlite3

conn = sqlite3.connect("watchlist.db")
c = conn.cursor()

def init_db():
    c.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year TEXT,
            watched INTEGER DEFAULT 0
        )
    ''')
    conn.commit()

def add_movie(title, year):
    c.execute("INSERT INTO movies (title, year) VALUES (?, ?)", (title, year))
    conn.commit()

def mark_watched(movie_id):
    c.execute("UPDATE movies SET watched = 1 WHERE id = ?", (movie_id,))
    conn.commit()

def get_all_movies():
    c.execute("SELECT * FROM movies")
    return c.fetchall()
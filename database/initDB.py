import sqlite3
import archives

conn = sqlite3.connect(archives.database)
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               password TEXT NOT NULL,
               email TEXT NOT NULL
               ) ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS posts(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               title TEXT NOT NULL,
               description TEXT NOT NULL
               ) ''')
cursor.execute('''
               CREATE TABLE IF NOT EXISTS comments(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               description TEXT NOT NULL,
                postId INTEGER NOT NULL
               ) ''')

conn.commit()
conn.close()    
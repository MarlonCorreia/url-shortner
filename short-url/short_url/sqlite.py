import sqlite3
import re

conn = sqlite3.connect('urls.db')
cursor = conn.cursor()

def create_schema():
    #criando a tabela (schema)

    cursor.execute("""
    CREATE TABLE urls (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            shortUrl TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')

    return

def insert_table(url, shortURL, id):

    conn.execute("""
        INSERT INTO urls(id, url, shortURL) VALUES (?, ?, ?)
    """, (id, url, shortURL) )

    conn.commit()
    
    return

#insert_table('https://twitch.com', '/ttt', 111)


def get_short_url(url_passed):

# lendo os dados
    cursor.execute("""
    SELECT url FROM urls
    """)

    db = cursor.fetchall()
    position = 0
    print(db[1])


    for url in db:
        if (url == url_passed):
            print(db[position][0])
        else:    
            position = position + 1
            #print(position)
            #print("false")

    return

get_short_url('https://twitch.com')

#Closing 
conn.close()

#toDo: find a way to compare sqlite response to a string. Possible solution: use List() and RegEX 
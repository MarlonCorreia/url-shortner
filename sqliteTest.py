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

# lendo os dados
cursor.execute("""
SELECT url FROM urls;
""")

for linha in cursor.fetchall():
    
    print(str(linha))
     
    if (linha == '(\'https://google.com\',)' ):
        print(linha)
    else:
        print("false")

#Closing 
conn.close()

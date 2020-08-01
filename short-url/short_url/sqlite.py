import sqlite3
import string
import random


def create_schema():

    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()
    #criando a tabela (schema)

    cursor.execute("""
    CREATE TABLE urls (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            shortUrl TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')

    conn.close()
    return

def insert_table(url):
    conn = sqlite3.connect('urls.db', check_same_thread=False)

    shortURL = get_random_string()

    conn.execute("""
        INSERT INTO urls(id, url, shortURL) VALUES (NULL, ?, ?)
    """, (url, shortURL) )

    conn.commit()
    conn.close()
    return shortURL



def get_shortUrl_by_url(url_passed):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

   # lendo os dados
    cursor.execute("""
    SELECT shortUrl FROM urls WHERE url = ?
    """, (url_passed,))
   
    response = cursor.fetchone()

    if (response is not None ):
        db = [i for i in response]
        return db[0]
    else:
        return insert_table(url_passed)    
  

def get_url_by_shortUrl(shortUrl_passed):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

# lendo os dados
    cursor.execute("""
    SELECT url FROM urls WHERE shortUrl = ?
    """, (shortUrl_passed,))

    response = cursor.fetchone()

    if (response is not None):
        db = [i for i in response]
        return db[0]
    else:
        return "ShortUrl not Found"


#Generate randon string to redirect
def get_random_string():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(4))
    return "/" + result_str

#Check if result_string isn't in use
def check_randon_string(result_str):
    return 'false'


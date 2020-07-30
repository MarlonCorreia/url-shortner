import sqlite3
import string
import random



def create_schema():

    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()
    #criando a tabela (schema)

    cursor.execute("""
    CREATE TABLE urls (
            url TEXT NOT NULL,
            shortUrl TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')

    conn.close()
    return

def insert_table(url):
    conn = sqlite3.connect('urls.db', check_same_thread=False)

    shortURL = '/' + get_random_string()

    conn.execute("""
        INSERT INTO urls(url, shortURL) VALUES (?, ?)
    """, (url, shortURL) )

    conn.commit()
    conn.close()
    return shortURL


def get_shortUrl_by_url(url_passed):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

# lendo os dados
    cursor.execute("""
    SELECT url FROM urls
    """)

    db = [i[0] for i in cursor.fetchall()] 
    position = 0

    for url in db:
        if (url == url_passed):
           conn.close() 
           return return_short_url(position)
        else:    
            position = position + 1
    conn.close()    
    return insert_table(url_passed)

def return_short_url(position):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

# lendo os dados
    cursor.execute("""
    SELECT shortUrl FROM urls
    """)

    db = [i[0] for i in cursor.fetchall()] 
    
    conn.close()
    return db[position]


def get_url_by_shortUrl(shortUrl_passed):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

# lendo os dados
    cursor.execute("""
    SELECT shortUrl FROM urls
    """)

    db = [i[0] for i in cursor.fetchall()] 
    position =0

    for shortUrl in db:
        if (shortUrl == '/' + shortUrl_passed):
           conn.close()
           return return_url(position)
        else:    
            position = position + 1
    conn.close()    
    return 

def return_url(position):
    conn = sqlite3.connect('urls.db', check_same_thread=False)
    cursor = conn.cursor()

# lendo os dados
    cursor.execute("""
    SELECT url FROM urls
    """)

    db = [i[0] for i in cursor.fetchall()] 
    conn.close()
    return db[position]


#Generate randon string to redirect
def get_random_string():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(4))
    return result_str

#Check if result_string isn't in use
def check_randon_string(result_str):
    return 'false'

print(get_url_by_shortUrl('/ykCg'))
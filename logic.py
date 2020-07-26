import random
import string



entry = "google.com"

maps = {'/yyy': 'https://youtube.com', '/ggg': 'https://google.com'}
short_url = list(maps.keys())
url = list(maps.values())

def get_short_url(url, short_url, entry):
    position = 0

    for url in url:
        if (url == entry):
            return short_url[position]
        else:
            position = position +1

    return "not found"

def get_url(url, short_url, entry):
    position = 0

    for short_url in short_url:
        if (short_url == '/' + entry):
            return url[position]
        else:
            position = position + 1

    return "/"

get_url(url, short_url, '/yyy')

#Generate randon string to redirect
def get_random_string():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(4))
    return result_str

#Check if result_string isn't in use
def check_randon_string(result_str):
    return 'false'


#store new new shortURL in maps
def insert_data_Base(url_from, url_to):
    return
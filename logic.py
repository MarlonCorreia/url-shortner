import random
import string



entry = "google.com"

maps = {'/yyy': 'https://www.youtube.com/', '/ggg': 'https://www.google.com/'}
#short_url = list(maps.keys())[0]
#url = list(maps.values())


def get_short_url(maps, entry):
    position = 0

    for url in list(maps.values()):
        if (url == entry):
            return list(maps.keys())[position]
        else:
            position = position +1

    return insert_maps(entry)

def get_url(maps, entry):
    position = 0

    for short_url in list(maps.keys()):
        if (short_url == '/' + entry):
            return list(maps.values())[position]
        else:
            position = position + 1

    return "/"


#Generate randon string to redirect
def get_random_string():
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(4))
    return result_str

#Check if result_string isn't in use
def check_randon_string(result_str):
    return 'false'


#store new new shortURL in maps
def insert_maps(entry):
    new_short_url = '/' + get_random_string()
    maps.update({new_short_url: entry})

    return new_short_url


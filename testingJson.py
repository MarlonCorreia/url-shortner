import json

#Writing json

new_mapping = [{"url_from": "test", "url_to": "test"}]

def apped_json(new_position):

    with open("maps.json", "a") as maps:
        json.dump(new_mapping, maps)
    return



#reading json

def read_json():
    
    with open("maps.json") as f:
        data = json.load(f)
        print(data)

    return


apped_json(new_mapping)
import json


def save_to_json(file, key, val):
    f = open(file)
    data = json.load(f)

    if key in data:
        return

    data[key] = val

    with open(file, 'w') as out:
        json.dump(data, out)


def extract_from_json(file, key):
    f = open(file)
    data = json.load(f)

    if key in data:
        return data[key]
    else:
        return None
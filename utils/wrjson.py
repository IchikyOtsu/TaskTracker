import json


def write_to_json_file(path, obj):
    with open(path, 'wt') as f:
        json.dump(obj, f)


def read_from_json_file(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        write_to_json_file(path, {})
        with open(path, 'r') as f:
            return json.load(f)


def create_new_idTask(path):
    db = read_from_json_file(path)
    for index in db:
        if db[index] == {}:
            return index
    return len(db)


# test = read_from_json_file("db.json")
# print(test["0"])

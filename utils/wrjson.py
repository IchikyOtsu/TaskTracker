import json


def write_to_json_file(path, obj):
    """
    Writes a JSON object to a file.

    Args:
        path (str): The file path where the JSON object will be written.
        obj (dict): The JSON object to write.
    """
    with open(path, 'wt') as f:
        json.dump(obj, f)


def read_from_json_file(path):
    """
    Reads a JSON object from a file. If the file does not exist, it creates an empty JSON file.

    Args:
        path (str): The file path from which to read the JSON object.

    Returns:
        dict: The JSON object read from the file.
    """
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        write_to_json_file(path, {})
        with open(path, 'r') as f:
            return json.load(f)


def create_new_idTask(path):
    """
    Creates a new task ID based on the existing IDs in the database.

    Args:
        path (str): The file path to the database.

    Returns:
        int: A new task ID.
    """
    db = read_from_json_file(path)
    for index in db:
        if db[index] == {}:
            return index
    return len(db)


# test = read_from_json_file("db.json")
# print(test["0"])

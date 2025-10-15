import json
from utils import wrjson
from utils import datefonc
pathdb = "db.json"


def print_task(task, db):
    """
    Prints the details of a task from the database.
    
    Args:
        task (str): The task identifier.
        db (dict): The database containing task information.
    """
    id = db[task]["id"]
    name = db[task]["name"]
    desc = db[task]["description"]
    status = db[task]["status"]
    print(
        f"id : {id}, name : {name}, description : {desc}, status : {status}")


def delete_from_ts(index):
    """
    Deletes a task from the database by its index.
    
    Args:
        index (int): The index of the task to delete.
    """
    db = wrjson.read_from_json_file(pathdb)
    db[index] = {}
    wrjson.write_to_json_file(pathdb, db)


def task_list(status="all"):
    """
    Lists tasks based on their status.
    
    Args:
        status (str): The status of tasks to list. Can be 'all', 'done', 'todo', or 'in-progress'.
    """
    db = wrjson.read_from_json_file(pathdb)
    for task in db:
        for index in task:
            index = int(index)
            if db[task] != {}:
                if status == "all":
                    if db[task]["status"]:
                        print_task(task, db)
                elif status == "done":
                    if db[task]["status"] == "done":
                        print_task(task, db)
                elif status == "todo":
                    if db[task]["status"] == "todo":
                        print_task(task, db)
                elif status == "in-progress":
                    if db[task]["status"] == "in-progress":
                        print_task(task, db)
    print("---")
    print(
        f"End of the list, if you can't see anythings there is probably no task with the status '{status}' in the database.")


def ts_mark_done(index):
    """
    Marks a task as done by its index.
    
    Args:
        index (int): The index of the task to mark as done.
    """
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "done"
    db[index]["statusId"] = "2"
    wrjson.write_to_json_file(pathdb, db)


def ts_mark_in_progress(index):
    """
    Marks a task as in progress by its index.
    
    Args:
        index (int): The index of the task to mark as in progress.
    """
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "in-progress"
    db[index]["statusId"] = "1"
    wrjson.write_to_json_file(pathdb, db)


def ts_mark_to_do(index):
    """
    Marks a task as to do by its index.
    
    Args:
        index (int): The index of the task to mark as to do.
    """
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "todo"
    db[index]["statusId"] = "0"
    wrjson.write_to_json_file(pathdb, db)


def ts_description_change(index, description):
    """
    Changes the description of a task by its index.
    
    Args:
        index (int): The index of the task to change.
        description (str): The new description for the task.
    """
    db = wrjson.read_from_json_file(pathdb)
    db[index]["description"] = description
    wrjson.write_to_json_file(pathdb,db)


class Task:
    def __init__(self, name):
        """
        Initializes a new task with the given name.
        
        Args:
            name (str): The name of the task.
        """
        current_timestamp = datefonc.get_current_time_intimestamp()
        newid = wrjson.create_new_idTask(pathdb)
        self.id = newid
        self.name = name
        self.description = None
        self.statusid = 0
        self.status = "todo"
        self.createAT = current_timestamp
        self.updateAT = current_timestamp

    def __str__(self):
        """
        Returns a string representation of the task.
        
        Returns:
            str: A string representation of the task.
        """
        idstr = f"'id':'{self.id}',"
        namestr = f"'name':'{self.name}',"
        descstr = f"'description':'{self.description}',"
        statusidstr = f"'statusId':'{self.statusid}',"
        statusstr = f"'status':'{self.status}',"
        createATstr = f"'createAT':'{self.createAT}',"
        updateATstr = f"'updateAT':'{self.updateAT}'"

        return "{"+idstr+descstr+statusidstr+statusstr+createATstr+updateATstr+"}"

    def class_to_json(self):
        """
        Converts the task instance to a JSON serializable dictionary.
        
        Returns:
            dict: A dictionary representation of the task.
        """
        json_object = {}
        json_object["id"] = self.id
        json_object["name"] = self.name
        json_object["description"] = self.description
        json_object["statusId"] = self.statusid
        json_object["status"] = self.status
        json_object["createAT"] = self.createAT
        json_object["updateAT"] = self.updateAT

        return json_object

    def add_new_task(self):
        """
        Adds the task to the database.
        """
        db = wrjson.read_from_json_file(pathdb)
        db[self.id] = self.class_to_json()
        wrjson.write_to_json_file(pathdb, db)

import json
from utils import wrjson
from utils import datefonc
pathdb = "db.json"


def print_task(task, db):
    id = db[task]["id"]
    name = db[task]["name"]
    desc = db[task]["description"]
    status = db[task]["status"]
    print(
        f"id : {id}, name : {name}, description : {desc}, status : {status}")


def delete_from_ts(index):
    db = wrjson.read_from_json_file(pathdb)
    db[index] = {}
    wrjson.write_to_json_file(pathdb, db)


def task_list(status="all"):
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
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "done"
    db[index]["statusId"] = "2"
    wrjson.write_to_json_file(pathdb, db)


def ts_mark_in_progress(index):
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "in-progress"
    db[index]["statusId"] = "1"
    wrjson.write_to_json_file(pathdb, db)


def ts_mark_to_do(index):
    db = wrjson.read_from_json_file(pathdb)
    db[index]["status"] = "todo"
    db[index]["statusId"] = "0"
    wrjson.write_to_json_file(pathdb, db)

def ts_description_change(index, description):
    db = wrjson.read_from_json_file(pathdb)
    db[index]["description"] = description
    wrjson.write_to_json_file(pathdb,db)


class Task:
    def __init__(self, name):
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
        idstr = f"'id':'{self.id}',"
        namestr = f"'name':'{self.name}',"
        descstr = f"'description':'{self.description}',"
        statusidstr = f"'statusId':'{self.statusid}',"
        statusstr = f"'status':'{self.status}',"
        createATstr = f"'createAT':'{self.createAT}',"
        updateATstr = f"'updateAT':'{self.updateAT}'"

        return "{"+idstr+descstr+statusidstr+statusstr+createATstr+updateATstr+"}"

    def class_to_json(self):
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
        db = wrjson.read_from_json_file(pathdb)
        db[self.id] = self.class_to_json()
        wrjson.write_to_json_file(pathdb, db)

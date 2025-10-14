import json
from utils import wrjson
from utils import datefonc


class Task:
    def __init__(self, name):
        current_timestamp = datefonc.get_current_time_intimestamp()
        newid = wrjson.create_new_idTask("db.json")
        self.id = newid
        self.name = name
        self.description = None
        self.statusid = 0
        self.status = "To Do"
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
        db = wrjson.read_from_json_file("db.json")
        db.append(self.class_to_json())
        wrjson.write_to_json_file("db.json", db)

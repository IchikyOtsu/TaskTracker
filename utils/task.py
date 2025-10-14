import json
import wrjson
import datefonc


class Task:
    def __init__(self, id):
        current_timestamp = datefonc.get_current_time_intimestamp()
        self.id = id
        self.description = None
        self.statusid = 0
        self.status = "To Do"
        self.createAT = current_timestamp
        self.updateAT = current_timestamp


TASK = Task(1)

print(TASK.createAT)

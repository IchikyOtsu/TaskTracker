import unittest
from utils import task


class TestTaskPriority(unittest.TestCase):
    def test_priority_initialization(self):
        t = task.Task('Priority Test')
        self.assertEqual(t.priority, 0)

    def test_priority_update(self):
        t = task.Task('Priority Test')
        t.add_new_task()
        # Change priority
        task.ts_change_priority(t.id, 2)
        # Read back from db
        from utils import wrjson
        db = wrjson.read_from_json_file(task.pathdb)
        self.assertEqual(db[t.id]['priority'], 2)


if __name__ == "__main__":
    unittest.main()

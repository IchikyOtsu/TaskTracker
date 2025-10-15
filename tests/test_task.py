import unittest
from utils import task

class TestTaskClass(unittest.TestCase):
    def test_task_initialization(self):
        t = task.Task('Test Task')
        self.assertEqual(t.name, 'Test Task')
        self.assertEqual(t.status, 'todo')
        self.assertIsNotNone(t.id)
        self.assertIsNotNone(t.createAT)
        self.assertIsNotNone(t.updateAT)

    def test_class_to_json(self):
        t = task.Task('Test Task')
        json_obj = t.class_to_json()
        self.assertEqual(json_obj['name'], 'Test Task')
        self.assertEqual(json_obj['status'], 'todo')

    def test_str_method(self):
        t = task.Task('Test Task')
        s = str(t)
        self.assertIn('name', s)
        self.assertIn('status', s)

if __name__ == "__main__":
    unittest.main()

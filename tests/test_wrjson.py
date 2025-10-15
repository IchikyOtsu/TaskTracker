import unittest
import os
from utils import wrjson


class TestWrJson(unittest.TestCase):
    def setUp(self):
        self.test_path = 'test_db.json'
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def tearDown(self):
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_write_and_read_json(self):
        data = {'1': {'id': 1, 'name': 'Test'}}
        wrjson.write_to_json_file(self.test_path, data)
        result = wrjson.read_from_json_file(self.test_path)
        self.assertEqual(result, data)

    def test_create_new_idTask(self):
        wrjson.write_to_json_file(self.test_path, {'0': {}, '1': {}})
        new_id = wrjson.create_new_idTask(self.test_path)
        self.assertIn(new_id, ['0', 2])


if __name__ == "__main__":
    unittest.main()

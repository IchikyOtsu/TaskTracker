import unittest
from utils import datefonc


class TestDateFonc(unittest.TestCase):
    def test_get_current_time(self):
        result = datefonc.get_current_time()
        self.assertIsNotNone(result)
        self.assertTrue(hasattr(result, 'year'))

    def test_get_current_time_intimestamp(self):
        result = datefonc.get_current_time_intimestamp()
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()

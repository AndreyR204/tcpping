import unittest
from tcping import app


class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(app.get_results(0, 1, 1), ZeroDivisionError)

    def test_wrongcount(self):
        self.assertEqual(app.ping_hosts('127.0.0.1', 80, 3), None)

    def test_wrongcount(self):
        self.assertEqual(app.get_results(3, 1, 1), None)

    def test_pinglocal(self):
        self.assertEqual(app.ping_hosts('127.0.0.1', 80, 3), None)


if __name__ == '__main__':
    unittest.main()

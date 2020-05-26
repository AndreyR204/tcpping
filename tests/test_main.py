import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_variables(self):
        self.assertEqual(main.host, main.args.host)

if __name__ == '__main__':
    unittest.main()

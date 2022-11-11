# Class Level SetUp and tearDown methods
import unittest


class TesTCaseDemo2(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("I will run once before every test")

    def test_case1(self):
        print("Test Case 1 Executed")

    def test_case2(self):
        print("Test Case 2 Executed")

    @classmethod
    def tearDown(cls):
        print("I will run once after every test")


if __name__ == "__main__":
    unittest.main(verbosity=1)

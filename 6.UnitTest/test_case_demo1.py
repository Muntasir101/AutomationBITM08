import unittest


class TestCaseDemo1(unittest.TestCase):

    def setUp(self):
        print("I will run once before every test")

    def test_case1(self):
        print("Test Case 1 Executed")

    def test_case2(self):
        print("Test Case 2 Executed")


if __name__ == "__main__":
    unittest.main(verbosity=1)

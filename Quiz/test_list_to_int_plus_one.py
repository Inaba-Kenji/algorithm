import unittest
from list_to_int_plus_one import list_to_int_plus_one


class TestListToIntPlusOne(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(list_to_int_plus_one([1]), 2)

    def test_case_2(self):
        self.assertEqual(list_to_int_plus_one([2, 3]), 24)

    def test_case_3(self):
        self.assertEqual(list_to_int_plus_one([8, 9]), 90)

    def test_case_4(self):
        self.assertEqual(list_to_int_plus_one([9, 9]), 100)

    def test_case_5(self):
        self.assertEqual(list_to_int_plus_one([0, 0, 0, 9, 9, 9, 9]), 10000)

    def test_case_empty(self):
        self.assertEqual(list_to_int_plus_one([0]), 1)

    def test_case_multiple_digits(self):
        self.assertEqual(list_to_int_plus_one([1, 2, 3]), 124)


# テストを実行
if __name__ == "__main__":
    unittest.main()

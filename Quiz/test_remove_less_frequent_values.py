import unittest
from collections import Counter
from typing import List


# テスト対象の関数
def remove_less_frequent_values(x: List[int], y: List[int]):
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x = [i for i in x if i != key_x]
            elif value_x > value_y:
                y = [i for i in y if i != key_x]
    return x, y


# テストケース
class TestRemoveLessFrequentValues(unittest.TestCase):
    def test_basic_case(self):
        x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
        y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
        expected_x = [1, 2, 3, 4, 4, 10]
        expected_y = [5, 5, 5, 6, 7, 8, 8, 10]
        result_x, result_y = remove_less_frequent_values(x, y)
        self.assertEqual(result_x, expected_x)
        self.assertEqual(result_y, expected_y)

    def test_no_common_elements(self):
        x = [1, 2, 3]
        y = [4, 5, 6]
        expected_x = [1, 2, 3]
        expected_y = [4, 5, 6]
        result_x, result_y = remove_less_frequent_values(x, y)
        self.assertEqual(result_x, expected_x)
        self.assertEqual(result_y, expected_y)

    def test_identical_lists(self):
        x = [1, 2, 3, 4, 5]
        y = [1, 2, 3, 4, 5]
        expected_x = [1, 2, 3, 4, 5]
        expected_y = [1, 2, 3, 4, 5]
        result_x, result_y = remove_less_frequent_values(x, y)
        self.assertEqual(result_x, expected_x)
        self.assertEqual(result_y, expected_y)

    def test_empty_lists(self):
        x = []
        y = []
        expected_x = []
        expected_y = []
        result_x, result_y = remove_less_frequent_values(x, y)
        self.assertEqual(result_x, expected_x)
        self.assertEqual(result_y, expected_y)


if __name__ == "__main__":
    unittest.main()

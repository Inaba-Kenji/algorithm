import unittest
from count_most_frequent import (
    get_most_frequent_string_v1,
    get_most_frequent_string_v2,
    get_most_frequent_string_v3,
)


class TestMostFrequentString(unittest.TestCase):
    def setUp(self):
        # テストで使用する入力文字列
        self.test_input = "This is a pen. This is an apple. Applepen."
        self.expected_output = ("p", 6)  # 出力の期待値

    def test_v1(self):
        result = get_most_frequent_string_v1(self.test_input)
        self.assertEqual(result, self.expected_output)

    def test_v2(self):
        result = get_most_frequent_string_v2(self.test_input)
        self.assertEqual(result, self.expected_output)

    def test_v3(self):
        result = get_most_frequent_string_v3(self.test_input)
        self.assertEqual(result, self.expected_output)

    def test_empty_string(self):
        empty_input = ""
        expected_output = ("", 0)  # 空文字列の場合
        for func in [
            get_most_frequent_string_v1,
            get_most_frequent_string_v2,
            get_most_frequent_string_v3,
        ]:
            with self.subTest(func=func):
                result = func(empty_input)
                self.assertEqual(result, expected_output)

    def test_no_alphabets(self):
        special_input = "   ... !!! $$$"
        expected_output = ("", 0)  # アルファベットがない場合
        for func in [
            get_most_frequent_string_v1,
            get_most_frequent_string_v2,
            get_most_frequent_string_v3,
        ]:
            with self.subTest(func=func):
                result = func(special_input)
                self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()

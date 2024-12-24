import unittest
from min_heap import MinHeap  # MinHeap クラスをインポート


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = MinHeap()

    def test_insert(self):
        self.min_heap.insert(5)
        self.min_heap.insert(6)
        self.min_heap.insert(2)
        self.assertEqual(self.min_heap.heap, [2, 6, 5])  # Min-Heap: [2, 6, 5]

    def test_get_min(self):
        self.min_heap.insert(5)
        self.min_heap.insert(6)
        self.min_heap.insert(2)
        self.assertEqual(self.min_heap._get_min(), 2)  # 最小値は2

    def test_extract_min(self):
        self.min_heap.insert(5)
        self.min_heap.insert(6)
        self.min_heap.insert(2)
        min_val = self.min_heap.extract_min()
        self.assertEqual(min_val, 2)  # 最小値は2
        self.assertEqual(self.min_heap.heap, [5, 6])  # 残り: [5, 6]

    def test_extract_min_empty(self):
        with self.assertRaises(IndexError):
            self.min_heap.extract_min()

    def test_get_min_empty(self):
        with self.assertRaises(IndexError):
            self.min_heap._get_min()

    def test_insert_and_extract(self):
        self.min_heap.insert(10)
        self.min_heap.insert(3)
        self.min_heap.insert(8)
        self.min_heap.insert(1)
        self.assertEqual(self.min_heap.extract_min(), 1)  # 最小値は1
        self.assertEqual(self.min_heap.extract_min(), 3)  # 次は3
        self.assertEqual(self.min_heap.extract_min(), 8)  # 次は8
        self.assertEqual(self.min_heap.extract_min(), 10)  # 次は10
        with self.assertRaises(IndexError):  # 全て削除後はエラー
            self.min_heap.extract_min()


if __name__ == "__main__":
    unittest.main()

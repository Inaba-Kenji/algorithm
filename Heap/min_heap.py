class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    # 値を挿入し、ヒープ条件を満たすように調整
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    # 最小値を削除して返し、ヒープ条件を満たすように調整
    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("ヒープが空です")
        if len(self.heap) == 1:
            return self.heap.pop()

        # 最小値をルートから取り出し、最後の要素をルートに移動
        min_value = self._get_min()
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    # 最小値を返す
    def _get_min(self):
        if len(self.heap) == 0:
            raise IndexError("ヒープが空です")
        return self.heap[0]

    # 親ノードと比較し、ヒープ条件を満たすまで上に移動
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self._heapify_up(parent_index)

    # 子ノードと比較し、ヒープ条件を満たすまで下に移動
    def _heapify_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[smallest]
        ):
            smallest = right_child

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self._heapify_down(smallest)


if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(5)
    min_heap.insert(6)
    min_heap.insert(2)
    print(min_heap.heap)

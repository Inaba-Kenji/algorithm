class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # ノードをリストの末尾に追加
    def append(self, data):
        new_node = Node(data)

        if not self.head:  # リストが空の場合
            self.head = new_node
            self.tail = new_node
        else:  # 既存のリストがある場合
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # ノードをリストの先頭に追加
    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # リストの内容を表示
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else " -> None\n")
            current = current.next

    # ノードを削除
    def delete(self, data):
        current = self.head

        while current:
            if current.data == data:
                # ノードが先頭の場合
                if current == self.head:
                    self.head = current.next
                    # 新しい先頭のprevをNoneに(リスト１つだけの場合のためにself.headがあるかの確認が必要)
                    if self.head:
                        self.head.prev = None
                # ノードが末尾の場合
                elif current == self.tail:
                    self.tail = current.prev
                    # 新しい末尾のnextをNoneに(リスト１つだけの場合のためにself.headがあるかの確認が必要)
                    if self.tail:
                        self.tail.next = None
                # 中間のノードの場合
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            # 次のノードに移動
            current = current.prev
            self.head, self.tail = self.tail, self.head

    def reverse_recursive(self):
        def _reverse(node):
            node.prev, node.next = node.next, node.prev
            # ベースケース: 次が None一番最後のノードに到達したことになる。
            # その一つ前のノードは次の先頭になるノードにあたる
            if not node.prev:
                self.head = node
                return
            # 次のノードを処理する
            _reverse(node.prev)

        if self.head:
            _reverse(self.head)
            self.head, self.tail = self.tail, self.head

    def sort(self):
        if not self.head or not self.head.next:
            return  # 要素が1つ以下の場合、何もする必要がない

        # Bubble Sortを使用してノードのデータを並び替え
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # データをスワップ
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next


# 双方向リストを作成
dll = DoublyLinkedList()

# データを追加
# dll.append(1)
# dll.append(2)
# dll.append(3)

dll.append(2)
dll.append(3)
dll.append(1)


# print("リスト (順方向):")
dll.display()

# print("リスト (逆方向):")
# dll.display_reverse()

# リストの先頭に追加
# dll.prepend(0)
# print("リストに先頭ノード 0 を追加:")
# dll.display()

# # ノードを削除
# dll.delete(2)
# print("ノード 2 を削除:")
# dll.display()

# # ノードを削除（先頭）
# dll.delete(0)
# print("ノード 0 を削除:")
# dll.display()

# # ノードを削除（末尾）
# dll.delete(3)
# print("ノード 3 を削除:")
# dll.display()

# dll.reverse()
# dll.display()

# dll.reverse_recursive()
# dll.display()

dll.sort()
dll.display()

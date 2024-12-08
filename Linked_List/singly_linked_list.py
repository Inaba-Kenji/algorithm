class Node:
    def __init__(self, data, next_node: None = None):
        self.data = data  # ノードのデータ
        self.next = next_node  # 次のノードへの参照


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # リストの最初のノード（初期状態では空）

    # リストの末尾に新しいノードを追加
    def append(self, data):
        new_node = Node(data)
        # リストが空の場合、最初のノードとして追加
        if not self.head:
            self.head = new_node
        else:
            # ノードが存在する場合は、最後のノードの次に追加する
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # リストの先頭に新しいノードを追加
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # 新しいノードが現在のヘッドを指すようにする
        self.head = new_node  # 新しいノードをヘッドにする

    # リストの全要素を表示
    def display(self):
        current = self.head
        if not current:
            print("このリストは空です")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print(f"{data}が見つかりませんでした。")
            return

        prev.next = current.next
        current = None

    # リストを逆順に並び替え
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev

            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            return _reverse_recursive(current, prev)

        # 一番最後の最後のノードをreturnしている 例:この場合だと30
        self.head = _reverse_recursive(self.head, None)

    # 連続した偶数のみreverseを実行する
    # 1 -> 8 -> 6 -> 4 -> 9
    # 4 -> 6 -> 8 => 8 -> 6 -> 4
    # start.next = nodeについて
    # start.nextは偶数の始まりの次の値この場合は4の次の値に連続して偶数ではなかった（この場合は9）が選ばれる

    # return prevについて
    # 偶数の終わりの部分(ここだと8)が先頭になるからnodeが偶数でなくなった時の一つ前であるprevを返してあげる

    # 連続した偶数の前の値(ここでだと1の次の値が)reverse_evenされて一番前になった(ここだと8の値が)node.nextになる
    # node.next = _reverse_even(node.next, node)
    def reverse_even(self):
        def _reverse_even(node, prev):
            if not node:
                return None

            if node.data % 2 == 0:  # 偶数部分の開始
                start = node
                while node and node.data % 2 == 0:  # 偶数部分を反転
                    next_node = node.next
                    node.next = prev
                    prev, node = node, next_node
                start.next = node  # 反転した偶数部分の終わりを接続
                return prev  # 偶数部分の新しい先頭を返す
            else:
                node.next = _reverse_even(node.next, node)
                return node

        self.head = _reverse_even(self.head, None)


linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(4)
linked_list.append(6)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.append(12)


# linked_list.display()  # 予想出力: 5 -> 10 -> 20 -> 30 -> None

# linked_list.reverse_recursive()
# linked_list.display()  # 予想出力: 30 -> 20 -> 10 -> 5 -> None

# linked_list.reverse()
# linked_list.display()  # 予想出力: 30 -> 20 -> 10 -> 5 -> None

# linked_list.delete(20)
# linked_list.display()  # 予想出力: 5 -> 10 -> 30 -> None

linked_list.display()  # 予想出力: 1 -> 4 -> 6 -> 8 -> 9 -> 10
linked_list.reverse_even()
linked_list.display()  # 予想出力: 1 -> 8 -> 6 -> 4 -> 9 -> 10

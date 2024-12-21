class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # 挿入のエントリーポイント。
    # self.rootを引数として渡す必要がなくなるため２つ分ける
    def insert(self, value) -> Node:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    # 再帰的な処理のロジック
    def _insert(self, node, value) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # 中間順トラバース (left, root, right)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    # 前順トラバース (root, left, right)
    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    # 後順トラバース (left, right, root)
    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node is not None:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def search(self, value: int) -> Node:
        return self._search(self.root, value)

    def _search(self, node: Node, value: int) -> Node:
        if node is None:
            return None

        if node.value == value:
            return node
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(7)
    print(bst.inorder())
    print(bst.preorder())
    print(bst.postorder())

    # 検索テスト
    test_values = [7, 15, 8]
    for test_value in test_values:
        result = bst.search(test_value)
        if result:
            print(f"値 {test_value} が見つかりました: ノードの値 = {result.value}")
        else:
            print(f"値 {test_value} は見つかりませんでした。")

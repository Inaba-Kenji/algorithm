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

    def search(self, value) -> Node:
        return self._search(self.root, value)

    def _search(self, node, value) -> Node:
        if node is None:
            return None

        if node.value == value:
            return node
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # ノードが見つかった場合
            # 片方しかnodeがないパターン
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 両方nodeがあるパターン
            # 削除対象ノードより大きい最小値
            min_larger_node = self.find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)
        return node

    # 部分木の最小ノードを探す
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == "__main__":
    # bst = BinarySearchTree()
    # bst.insert(4)
    # bst.insert(2)
    # bst.insert(6)
    # bst.insert(1)
    # bst.insert(3)
    # bst.insert(7)
    # print(bst.inorder())
    # print(bst.preorder())
    # print(bst.postorder())

    # # 検索テスト
    # test_values = [7, 15, 8]
    # for test_value in test_values:
    #     result = bst.search(test_value)
    #     if result:
    #         print(f"値 {test_value} が見つかりました: ノードの値 = {result.value}")
    #     else:
    #         print(f"値 {test_value} は見つかりませんでした。")

    # ノードを挿入
    bst = BinarySearchTree()
    for value in [10, 5, 15, 3, 7, 12, 20]:
        bst.insert(value)

    print("削除前の中間順巡回:", bst.inorder())

    # テストケース: ノードを削除
    bst.delete(3)  # 葉ノードの削除
    print("3を削除後の中間順巡回:", bst.inorder())

    bst.delete(15)  # 1つの子を持つノードの削除
    print("15を削除後の中間順巡回:", bst.inorder())

    bst.delete(10)  # 2つの子を持つノードの削除
    print("10を削除後の中間順巡回:", bst.inorder())

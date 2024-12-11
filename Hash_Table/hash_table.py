import hashlib


class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        # キーがすでに存在する場合は値を更新
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                # 通常はhash関数では一意の値が求まるはずなので一つだけでよい
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# # ハッシュテーブルを作成
ht = HashTable()

# # データを挿入
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)
ht.insert("grape", 400)
ht.insert("melon", 500)

# ハッシュテーブルの内容を表示
# print("Before deletion:")
ht.display()

# # データを検索
print("\nSearch 'apple':", ht.search("apple"))
print("Search 'grape':", ht.search("grape"))
print("Search 'kiwi':", ht.search("kiwi"))  # 存在しないキー

# # データを削除
ht.delete("banana")
ht.delete("melon")

# ハッシュテーブルの内容を再表示
print("\nAfter deletion:")
ht.display()

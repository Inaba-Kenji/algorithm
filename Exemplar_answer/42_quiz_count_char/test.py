import operator
from typing import Tuple

def count_chars_v1(strings: str) -> Tuple[str, int]:
    # 小文字に変換する
    strings = strings.lower()
    # 空のリストを作成
    l = []
    for char in strings:
        # スペース以外だった場合
        if not char.isspace():
            l.append((char, strings.count(char)))

    return max(l, key=operator.itemgetter(1))

if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(s))

# for item in l:
#     if max_value is None or item[1] > max_value:
#         max_value = item[1]
#         max_item = item
# print(max_item)

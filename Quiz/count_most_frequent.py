# 最も多く出現する文字列をカウントする　小さい場合はどちらでもよい
# Input: 'This is a pen. This is an apple. Applepen.'
# Output: ('p', 6)

import operator
from typing import Counter, Tuple


def get_most_frequent_string_v1(strings: str) -> Tuple[str, int]:
    # 入力が空文字列またはアルファベットが含まれていない場合
    if not any(c.isalpha() for c in strings):
        return "", 0

    strings = strings.lower()
    l = []
    for char in strings:
        if not char.isspace():
            l.append((char, strings.count(char)))

    return max(l, key=operator.itemgetter(1))


def get_most_frequent_string_v2(strings: str) -> Tuple[str, int]:
    # 入力が空文字列またはアルファベットが含まれていない場合
    if not any(c.isalpha() for c in strings):
        return "", 0

    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


def get_most_frequent_string_v3(strings: str) -> Tuple[str, int]:
    # 入力が空文字列またはアルファベットが含まれていない場合
    if not any(c.isalpha() for c in strings):
        return "", 0

    strings = strings.lower()
    d = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]

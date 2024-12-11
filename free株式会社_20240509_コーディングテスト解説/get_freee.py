# 問題1-1

# 文字列 S が与えられます。S から f を1つ、r を1つ、e を3つ抜き出して freee という文字列を作ります。
# freee という文字列は最大何個作れますか？

# 制約
# 1 ≦ |S| ≦ 10^5 ( |S| は S の文字列の長さとする )

# 入力例
# serfefeereeo

# 出力例
# 2

from collections import Counter
from typing import Optional


def get_freee(S: str) -> Optional[int]:
    if not S:
        return None

    count_f = count_r = count_e = 0

    for s in S:
        if s == "f":
            count_f += 1
        elif s == "r":
            count_r += 1
        elif s == "e":
            count_e += 1

    return min(count_f, count_r, count_e // 3)


def get_freee2(S: str) -> Optional[int]:
    if not S:
        return None

    counts = Counter(S)
    count_f = counts.get("f", 0)
    count_r = counts.get("r", 0)
    count_e = counts.get("e", 0)

    return min(count_f, count_r, count_e // 3)


if __name__ == "__main__":
    S = "serfefeereeo"
    print(get_freee(S))
    print(get_freee2(S))

# freee
# f = 1
# r = 1
# e = 3

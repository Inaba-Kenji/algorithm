# Symmetric
# 左右対称ものを出力したい
# Input [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
# Output [(5, 3), (7, 4)]

from typing import List, Iterator, Tuple


def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for first, second in pairs:
        if cache.get(second) == first:
            yield (first, second)
        else:
            cache[first] = second


if __name__ == "__main__":
    pairs = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    for pair in find_pair(pairs):
        print(pair)

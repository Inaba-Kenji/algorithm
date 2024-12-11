# 1. Input: [11, 2, 5, 9, 10, 3] 12 => Output: (2, 10) or None
# 2. Input: [11, 2, 5, 9, 10, 3]    => Output: (11, 9) or None 11 + 9 = 2 + 5 + 10 + 3

from typing import List, Tuple, Optional


def get_pair(numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()
    for num in numbers:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


# もう片方のペアを逃さない設計
def get_pair_half_sum(numbers: List[int]) -> Optional[Tuple[int, int]]:
    sum_numbers = sum(numbers)
    # 半分に割れない場合は存在しない
    if sum_numbers % 2 != 0:
        return
    half_sum = int(sum_numbers / 2)

    cache = set()
    for num in numbers:
        cache.add(num)
        # もしペアがある場合は、valの値がそのペア同士の値になる ex(20 - 11 = 9, 20 - 9 = 11)
        # だから20 - 11 = 9のパターンで見つからなくても、もう一つの20 - 9 = 11パターンで見つかる。
        # cacheの中に見つからないパターンの11の値が先にいるから
        val = half_sum - num
        if val in cache:
            return val, num


if __name__ == "__main__":
    numbers = [11, 2, 5, 9, 10, 3]
    target = 12
    print(get_pair(numbers, target))
    print(get_pair_half_sum(numbers))

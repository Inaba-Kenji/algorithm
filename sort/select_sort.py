import random
from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_index = i
        # この範囲の中で一番小さい値を見つける
        for j in range(i + 1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j

        # 全部確認したら、iの値とその範囲で最も小さい値を入れ替える
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(selection_sort(nums))

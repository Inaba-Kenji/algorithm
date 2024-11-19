import random
from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    # limitの線の部分を表している 内側の比べる範囲を小さくしていっている。
    for i in range(len(numbers)):
        # limitの線の範囲内で前後の数字を比較している
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(bubble_sort(nums))

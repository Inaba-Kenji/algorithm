import random
from typing import List


def couting_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    # countは0を含めて配列の中のmaxまで必要だから+1する
    counts = [0] * (max_num + 1)
    result = [0] * len(numbers)

    # indexの数字と同じ値がいくつあるかを数える
    for num in numbers:
        counts[num] += 1

    # indexの数字が前から何番目かを表す。
    # 同じ数字が複数ある場合はその数字の一番後ろの値が何番目かを表す。
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = numbers[i]
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(couting_sort(nums))

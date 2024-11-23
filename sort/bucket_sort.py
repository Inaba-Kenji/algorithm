import random
from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = temp

    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]
    # バケットに数字を割りふって
    for num in numbers:
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            # numbersの最大値だった場合は商がsizeより1大きいので、-1一番後ろの配列に挿入する
            buckets[size - 1].append(num)

    for i in range(size):
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        result += buckets[i]

    return result


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    print(nums)
    print(bucket_sort(nums))

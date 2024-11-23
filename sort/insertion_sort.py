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


if __name__ == "__main__":
    # nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [1, 7, 2, 3, 8, 5]
    print(nums)
    print(insertion_sort(nums))

import random
from typing import List


def genome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0

    while index < len_numbers:
        if index == 0:
            index += 1
        if numbers[index] >= numbers[index - 1]:
            index += 1
        else:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            index -= 1
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(genome_sort(nums))

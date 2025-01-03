from typing import List


def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(6)]
    # nums = [5, 4, 1, 8, 7, 3, 2, 9]
    # nums = [2, 1, 3, 6, 5, 5, 7]
    # nums = [1, 5, 7, 9, 4, 2, 6]
    print(nums)
    print(merge_sort(nums))

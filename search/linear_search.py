from typing import List, NewType

IndexNum = NewType("IndexNum", int)


def linear_search(numbers: List[int], value: int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1


if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    print(linear_search(nums, 15))

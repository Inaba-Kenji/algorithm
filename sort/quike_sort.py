from typing import List


# ピボットを基準にして２つのグループに分ける
# それぞれのグループをさらにリストが１つの要素になるまで再起的に繰り返す
def partition(numbers: List[int], low: int, hight: int) -> int:
    # iはpivotの値より小さい値のindexを表している(-1は初回の比較のため)
    i = low - 1
    pivot = numbers[hight]

    for j in range(low, hight):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    i += 1
    numbers[i], numbers[hight] = numbers[hight], numbers[i]
    return i


def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index - 1)
            _quick_sort(numbers, partition_index + 1, high)

    _quick_sort(numbers, 0, len(numbers) - 1)
    return numbers


if __name__ == "__main__":
    import random

    nums = [random.randint(0, 1000) for _ in range(6)]
    # nums = [1, 8, 3, 9, 4, 5, 7]
    # nums = [2, 1, 3, 6, 5, 5, 7]
    # nums = [1, 5, 7, 9, 4, 2, 6]
    print(quick_sort(nums))

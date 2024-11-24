import random
from typing import List


# ギャップ（間隔）を徐々に縮めながらソートを行うことで、挿入ソートの効率を改善します。
def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2

    while gap > 0:
        for i in range(gap, len_numbers):
            temp = numbers[i]
            j = i

            # j >= gapは0より小さい値と比較しないため
            # numbers[j-gap] > tempは配列の間をギャップの数だけ前に戻って比較する
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2

    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(shell_sort(nums))

# Bogosortは、基本的に「ランダムな順番に並べて、並べ替えが完了しているかをチェックする」


import random
from typing import List


# 昇順確認のため
def is_sorted_ascending(numbers: List[int]) -> bool:
    # 省略記法(リスト内包表記)
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    # for i in range(len(numbers) - 1):
    #     if numbers[i] > numbers[i + 1]:
    #         return False
    # return True


# bogosortでの並び替え
def bogo_sort(numbers: List[int]) -> List[int]:
    while not is_sorted_ascending(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))

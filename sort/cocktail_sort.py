import random
from typing import List


# limitを前と後ろ両方に置いて両方から範囲を狭めて並び替えを実施する
def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True
    start_limit = 0
    end_limit = len_numbers - 1

    while swapped:
        swapped = False
        # 左から右へlimitの範囲で比較する
        for i in range(start_limit, end_limit):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        # 左から右へlimitの範囲で比較した時にswappedされたか確認
        if not swapped:
            break

        # swappedされていない時は右から左でlimitの範囲で確認をするので初期化とlimitの範囲を狭める
        swapped = False
        end_limit = end_limit - 1

        # iの値はi+1をするので最後尾の配列を指定するのではなくて、最後尾-1下値をiにしたい
        # 右から左へlimitの範囲で比較する
        for i in range(end_limit - 1, start_limit - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        # swappedに関しては、whileの直後で初期化されるのでここではfalseにしない
        start_limit = start_limit + 1

    return numbers


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(nums)
    print(cocktail_sort(nums))

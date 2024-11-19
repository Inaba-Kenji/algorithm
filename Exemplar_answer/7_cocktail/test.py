from typing import List


def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    # whileの処理に入るため
    swapped = True
    # 左のlimitの位置
    start = 0
    # 右のlimitの位置
    end = len_numbers - 1
    while swapped:
        # 初期化
        swapped = False
        # 左から右への並び替え
        for i in range (start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i] , numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        # 並び替えがないなら並び終えているので処理を抜ける
        if not swapped:
            break
        # 初期化
        swapped = False
        # 右から左へ並び替えを開始する時にlimitが変更されるため
        end = end - 1
        # limitが指している配列の一つ前のindex番号を示す
        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i] , numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(cocktail_sort(nums))

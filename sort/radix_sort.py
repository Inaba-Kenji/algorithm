import random
from typing import List


def couting_sort(numbers: List[int], place: int) -> List[int]:
    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        # 取り出したい部分を一の位にくるようにして、%10すればその桁の値を取得できる
        # 1.num / placeで取得したい桁数の値を一の位で取得できるようにする
        # 2.%10で一の位の値が取得できる
        index = int(num / place) % 10
        counts[index] += 1

    for i in range(1, 10):
        counts[i] += counts[i - 1]

    i = len(numbers) - 1
    while i >= 0:
        index = int(numbers[i] / place) % 10
        # counts[index]だと自分が何番目に来ればいいかを表しているから、resultだと-1になる
        # 例えば7番目だった場合は、resultの配列は0からスタートしているから6にその数字を入れないとだめ
        result[counts[index] - 1] = numbers[i]
        counts[index] -= 1
        i -= 1

    return result


def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    place = 1

    while max_num > place:
        numbers = couting_sort(numbers, place)
        place *= 10

    return numbers


if __name__ == "__main__":
    # nums = [random.randint(0, 1000) for _ in range(10)]
    nums = [24, 10, 11, 324, 201, 101, 55]
    print(nums)
    print(radix_sort(nums))

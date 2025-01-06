# [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15] => [1, 3, 5, 7, 10, 12, 15]

# 下記はなし
# numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
# print(list(set(numbers)))


from typing import List


def delete_duplicate_v1(numbers: List[int]) -> None:
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# 数字が並び替えてある場合
def delete_duplicate_v4(numbers: List[int]) -> None:
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i -= 1
    return numbers


if __name__ == "__main__":
    numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    # print(delete_duplicate_v1(numbers))
    print(delete_duplicate_v4(numbers))

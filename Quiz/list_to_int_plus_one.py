# [1] => [2] => 2
# [2, 3] => [2, 4] => 24
# [8, 9] => [9, 0] => 90
# [9, 9] => [1, 0, 0] => 100
# [0, 0, 0, 9, 9, 9, 9] => [1, 0, 0, 0, 0] => 10000

# 下記はなしとする
# numbers = [1, 2, 3]
# print(int("".join([str(i) for i in numbers])) + 1)

from typing import List


def list_to_int_plus_one(numbers: List[int]) -> int:
    answer = 0

    for digit in numbers:
        answer = answer * 10 + digit
    return answer + 1

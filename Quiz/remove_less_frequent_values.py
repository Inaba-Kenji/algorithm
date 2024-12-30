# input x: [1, 2, 3, 4, 4, 5, 5, 8, 10] y:  [4, 5, 5, 5, 5, 6, 7, 8, 8, 10]
# output: x: [1, 2, 3, 4, 4, 10] y:  [5, 5, 5, 5, 6, 7, 8, 8, 10]


from collections import Counter
from typing import List


def remove_less_frequent_values(x: List[int], y: List[int]):
    counter_x = Counter(x)
    counter_y = Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                # 下記だと元のリストに影響を与えるから影響範囲が大きい可能性があるから慎重に
                # x[:] = [i for i in x if i != key_x]
                # 該当のkey以外の値をxに入れる(yより該当の値が少なかったのでxから取り除く)
                answer_x = [i for i in x if i != key_x]
            elif value_x > value_y:
                # 下記だと元のリストに影響を与えるから影響範囲が大きい可能性があるから慎重に
                # y[:] = [i for i in y if i != key_y]
                # 該当のkey以外の値をyに入れる(xより該当の値が少なかったのでyから取り除く)
                answer_y = [i for i in y if i != key_x]
    return answer_x, answer_y


if __name__ == "__main__":
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print("x = ", x)
    print("y = ", y)
    print(remove_less_frequent_values(x, y))

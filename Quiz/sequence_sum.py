# 1.Maximum subarray sum
# Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
# output 14 (3, 6, -1, 2, 4)

# 2.Maximum circular subarray sum
# Input [1, -2, 3, 6, -1, 2, 4, -5, 2]
# output 15 (2, 1, -2, 3, 6, -1, 2, 4)


from typing import List


# 通常部分配列の最大合計
def get_max_min_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0

    for num in numbers:
        # 取得した数字から始めるのかorこれまでの値に追加するのか選択する
        sum_sequence = operator(num, sum_sequence + num)
        # これまでに見つかった部分配列の最大合計と現在の部分配列の合計を比較する
        # これまでに見つかった部分配列の最大合計値を保存しておく
        result_sequence = operator(result_sequence, sum_sequence)
    return result_sequence


# 考え方
# 循環部分配列の最大合計は 配列全体の合計 - 最小部分配列の合計
# 最終結果は以下のいずれか：
# 通常の最大部分配列の合計 or 循環部分配列の最大合計


# 循環部分配列の最大合計
def find_max_circular_sequence_sum(numbers: List[int]) -> int:
    max_sequence_sum = get_max_min_sequence_sum(numbers)
    max_ciruclar_sum = sum(numbers) - get_max_min_sequence_sum(numbers, min)
    return max(max_sequence_sum, max_ciruclar_sum)


if __name__ == "__main__":
    numbers = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    print(get_max_min_sequence_sum(numbers))
    print(find_max_circular_sequence_sum(numbers))

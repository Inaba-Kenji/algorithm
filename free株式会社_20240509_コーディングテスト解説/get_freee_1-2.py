# 問題1-2
# 文字列 S が与えられます。S から f を1つ、r を1つ、e を3つ抜き出して元の順番を保ったまま freee とい
# う文字列を作ります。freee という文字列は最大何個作れますか？
# 制約
# 1 ≦ |S| ≦ 10^5 ( |S| は S の文字列の長さとする )
# 入力例
# frefseereoeeeeerf
# 出力例
# 2


from typing import Optional


def get_free(S: str):
    count_f = count_fr = count_e = count_freee = 0

    for char in S:
        if char == "f":
            count_f += 1
        elif char == "r" and count_f > 0:
            count_fr += 1
            count_f -= 1
        elif char == "e" and count_fr > 0:
            count_e += 1
            if count_e == 3:
                count_fr -= 1
                count_e -= 3
                count_freee += 1
    return count_freee


def test_get_free():
    test_cases = [
        # テストケース: (入力, 期待される出力)
        ("frefseereoeeeeerf", 2),  # 元の例: freeeが2回構成できる
        ("freee", 1),  # ちょうど1つのfreeeが作れる
        ("fffrrreeeeeeeeeee", 3),  # f, r, eが十分ある場合
        ("", 0),  # 空文字列
        ("fr", 0),  # 必要なeが足りない
        ("eeee", 0),  # f, rがない場合
        ("frfreeefreee", 2),  # 必要なfreeeが2つ含まれる
        ("frrreeeeee", 1),  # fが足りない場合
        ("ffrreeeeee", 2),  # rが足りない場合
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = get_free(input_str)
        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(
            f"Test case {i + 1} passed: input='{input_str}', expected={expected}, got={result}"
        )


if __name__ == "__main__":
    # # 入力例
    # S1 = "frefseereoeeeeerf"
    # print(get_free(S1))  # 出力: 2
    # S2 = "freee"
    # print(get_free(S2))  # 出力: 1
    # S3 = "fffrrreeeeeeeeeee"
    # print(get_free(S3))  # 出力: 3
    test_get_free()

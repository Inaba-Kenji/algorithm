# jsonのカッコのフォーマットを正しいか判定する

# 1.次のようなフォーマットもjson形式としはだめ([)]
# 2.最初の]が入ってきてもfalse
# 3.最後のところで]とか[が残ってもfalseにする


def validate_format(chars: str) -> bool:
    lookup = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            # 一番最初に閉じるカッコが来た場合
            if not stack:
                return False
            # カッコの閉じる順番がおかしい時 例：([)]のような
            if char != stack.pop():
                return False
    # スタックの中に中身がある場合
    if stack:
        return False

    return True


if __name__ == "__main__":
    test_cases = [
        ("{}", True),  # 正しいフォーマット
        ("[]", True),  # 正しいフォーマット
        ("()", True),  # 正しいフォーマット
        ("{[()]}", True),  # ネストされた正しいフォーマット
        ("[{()}]", True),  # ネストされた正しいフォーマット
        ("[", False),  # 開き括弧が閉じていない
        ("]", False),  # 最初に閉じ括弧が来るのは不正
        ("[}", False),  # 閉じ括弧の種類が異なる
        ("([)]", False),  # カッコの閉じる順番が不正
        ("{[()]", False),  # 閉じ括弧が不足
        ("{[(])}", False),  # 閉じ括弧の種類と順番が不正
        ("", True),  # 空文字列（特に問題なし）
        ("[[[[", False),  # 開き括弧が多すぎる
        ("]]]]", False),  # 閉じ括弧が多すぎる
    ]

    for j, expected in test_cases:
        result = validate_format(j)
        print(
            f"Test case: {j}, Expected: {expected}, Got: {result}, Passed: {result == expected}"
        )

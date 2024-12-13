# 問題2-1
# 制約
# 0 ≦ N ≦ 2×10^9
# 2 ≦ M ≦ 5×10^3
# 0 ≦ A_i ≦ 10^9

# 入力例
# 友達とクリスマスプレゼントの交換会を行います。
# プレゼントは1人2つ選ぶ事になっており、合計の金額は N 円以下に収めないといけません。
# 候補として M 個のプレゼントがあり、i番目のプレゼントの値段は A_i 円です。
# 重複しないようにプレゼントを 2つ選んだ時、予算 N 円以下となる組み合わせはいくつありますか？

# 500 5
# 100 200 300 400 500

# 出力例 4


def find_budget_combinations(total_price, total_gifts, gift_prices):
    answer = 0
    for i in range(total_gifts - 1):
        for j in range(i + 1, total_gifts):
            if gift_prices[i] + gift_prices[j] <= total_price:
                answer += 1
    return answer


if __name__ == "__main__":
    total_price = 500
    total_gifts = 5
    gift_prices = [100, 200, 300, 400, 500]
    print(find_budget_combinations(total_price, total_gifts, gift_prices))

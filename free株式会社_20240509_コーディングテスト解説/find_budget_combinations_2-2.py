# 問題2-2
# 友達とクリスマスプレゼントの交換会を行います。
# プレゼントは1人2つ選ぶ事になっており、合計の金額は N 円以下に収めないといけません。
# 候補として M 個のプレゼントがあり、i番目のプレゼントの値段は A_i 円です。
# 重複しないようにプレゼントを 2つ選んだ時、予算 N 円以下となる組み合わせはいくつありますか？

# 制約(問題2-1 と比較して、プレゼントの候補数 M が大きくなった)
# 0 ≦ N ≦ 2×10^9
# 2 ≦ M ≦ 2×10^5
# 0 ≦ A_i ≦ 10^9

# 入力例
# 500 5
# 100 200 300 400 500

# 出力例 4


def find_budget_combinations(total_price, total_gift, gift_prices):
    sorted(gift_prices)
    answer = 0

    for i in range(total_gift - 1):
        for j in range(i + 1, total_gift):
            if gift_prices[i] + gift_prices[j] <= total_price:
                answer += 1
            else:
                break
    return answer


def find_budget_combinations2(total_price, total_gift, gift_prices):
    gift_prices.sort()
    left, right = 0, total_gift - 1
    count = 0

    while left < right:
        if gift_prices[left] + gift_prices[right] <= total_price:
            # 条件を満たす場合、leftからrightまでの全てが有効
            count += right - left
            left += 1
        else:
            # 条件を満たさない場合、rightを左に移動
            right -= 1
    return count


if __name__ == "__main__":
    total_price = 500
    total_gift = 5
    gift_prices = [100, 200, 300, 400, 500]
    print(find_budget_combinations(total_price, total_gift, gift_prices))
    print(find_budget_combinations2(total_price, total_gift, gift_prices))

def snake_v1(chars: str) -> None:
    results = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1

    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        results[insert_index].append(s)

        # 空白を挿入
        for result_index in result_indexes - {insert_index}:
            results[result_index].append(" ")

    # 各行を表示
    for line in results:
        print("".join(line))


def snake_v2(chars: str, num_row: int) -> None:
    if num_row <= 0:
        raise ValueError("Number of rows must be greater than 0")

    def pos(i):
        return i + 1

    def neg(i):
        return i - 1

    results = [[] for _ in range(num_row)]
    insert_index = int(num_row / 2)
    op = neg

    for s in chars:
        results[insert_index].append(s)

        # 他の行には空白を追加
        for i in range(num_row):
            if i != insert_index:
                results[i].append(" ")

        if insert_index == 0:
            op = pos
        if insert_index >= num_row - 1:
            op = neg
        insert_index = op(insert_index)

    # 各行を表示
    for line in results:
        print("".join(line))


if __name__ == "__main__":
    # numbers = [str(i) for i in range(10)] * 5
    # string = "".join(numbers)
    # snake_v1(string)

    # numbers = [str(i) for i in range(10)] * 5
    # string = "".join(numbers)
    # row = 3
    # snake_v2(string, row)

    import string

    alpahbet = [s for s in string.ascii_lowercase] * 2
    string = "".join(alpahbet)
    row = 10
    snake_v2(string, row)

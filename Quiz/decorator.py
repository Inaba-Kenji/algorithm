import time

# memo
# 1.memoize(test)()
# 2._wrapper()が実行
# 3._wrapper()には自動で元の関数の引数が渡される


# def memoize(f):
#     def _wrapper():
#         print("before")
#         r = f(n)
#         print("after")
#         return r

#     return _wrapper


# @memoize
# def test(n):
#     print("test")


def memoize(f):
    cache = {}

    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return _wrapper


@memoize
def long_func(num: int) -> int:
    r = 0
    for i in range(10000000):
        r += num * i
    return r


if __name__ == "__main__":
    for i in range(10):
        print(long_func(i))

    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)

from typing import List

def all_perms(elements: List[int]) -> List[List[int]]:
    first = elements[0:1]
    rest = elements[1:]
    for i in range(len(elements)):
        print(rest[:i] + first + rest[i:])


if __name__ == '__main__':
    all_perms([1, 2, 3,])

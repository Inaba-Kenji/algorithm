from collections import deque
from typing import Deque

def reverse(queue: Deque) -> Deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    return new_queue


if __name__ == '__main__':
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(reverse(q))

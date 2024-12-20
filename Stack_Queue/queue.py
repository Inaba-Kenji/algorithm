class Queue:

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data) -> None:
        self.queue.append(data)

    def dequeue(self) -> any:
        if self.queue:
            return self.queue.pop(0)
        raise IndexError("キューが空です")


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.queue)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.queue)

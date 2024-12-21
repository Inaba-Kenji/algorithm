class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self) -> None:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack size: {stack.size()}")  # 出力: Stack size: 3
    print(f"Top element: {stack.peek()}")  # 出力: Top element: 3
    print(f"Popped element: {stack.pop()}")  # 出力: Popped element: 3
    print(f"Is stack empty? {stack.is_empty()}")  # 出力: Is stack empty? False


class Stack[T]:
    def __init__(self):
        self.elements: list[T] = []

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        if not self.elements:
            raise IndexError('Stack is empty')
        return self.elements.pop()

def main():
    number_stack = Stack[int]()
    str_stack = Stack[str]()

    number_stack.push(10)
    print(number_stack.pop())
    str_stack.push('a')
    print(str_stack.pop())

if __name__ == '__main__':
    main()
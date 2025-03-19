from typing import Callable

def filter_elements[T](elements: list[T], condition_fn: Callable[[T], bool]) -> list[T]:
    return [element for element in elements if condition_fn(element)]


def main() -> None:
    print(filter_elements([1, 2, 3, 4], lambda x: x > 1))

if __name__ == '__main__':
    main()
from typing import Callable

def filter_elements[T](elements: list[T], condition_fn: Callable[[T], bool]) -> list[T]:
    return [element for element in elements if condition_fn(element)]

def process_pairs[K, V](data: dict[K, V], modifier_fn: Callable[[V], V]) -> dict[K, V]:
    return {key: modifier_fn(V) for key, V in data.items()}


def main() -> None:
    print(filter_elements([1, 2, 3, 4], lambda x: x > 1))
    print(process_pairs({'a': 1, 'b': 2, 'c': 3}, lambda x: x * 2))

if __name__ == '__main__':
    main()
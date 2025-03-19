from typing import Callable

def filter_elements[T](elements: list[T], condition_fn: Callable[[T], bool]) -> list[T]:
    return [element for element in elements if condition_fn(element)]

def process_pairs[K, V](data: dict[K, V], modifier_fn: Callable[[V], V]) -> dict[K, V]:
    return {key: modifier_fn(V) for key, V in data.items()}

def merge_items[T1, T2, T3](items1: T1, items2: T2, items3: T3) -> tuple[T1, T2, T3]:
    return items1, items2, items3


def main() -> None:
    print(filter_elements([1, 2, 3, 4], lambda x: x > 1))
    print(process_pairs({'a': 1, 'b': 2, 'c': 3}, lambda x: x * 2))
    print(merge_items(1, 'a', [22, 33]))

if __name__ == '__main__':
    main()
from typing import Callable

def filtered_type[T](elements: list[T], condition_fn: Callable[[T], bool]) -> T:
    return [element for element in elements if condition_fn(element)]

def process_pairs[K, V](data: dict[K, V], modifier_fn: Callable[[V],V]) -> dict[K, V]:
    return {key: modifier_fn(value) for key, value in data.items()}

def merge_items[T1, T2, T3](items1: T1, items2: T2, items3: T3) -> tuple[T1, T2, T3]:
    return items1, items2, items3


def main() -> None:
    print(filtered_type([1, 2, 3, 4], lambda x: x >= 2))
    print(process_pairs({'a': 1, 'b': 2, 'c': 3, 'd': 4}, lambda x: x * 2))
    print(merge_items('a', 33, {'a': 3}))

if __name__ == '__main__':
    main()

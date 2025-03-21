from typing import Callable, Any
import time


def measure_execution_time[T](fun: Callable[..., T]) -> Callable[..., T]:
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = time.time()
        print(f'Calling {fun.__name__} with {args}, {kwargs}')
        result = fun(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

def main() -> None:
    pass

if __name__ == '__main__':
    main()
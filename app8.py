from typing import Callable, Any
import time

type DataCallable[T] = Callable[..., T]


def measure_execution_time[T](fun: DataCallable) -> DataCallable:
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start_time = time.time()
        print(f'Calling {fun.__name__} with {args}, {kwargs}')
        result = fun(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@measure_execution_time
def do_action(a: int, b:int) -> int:
    time.sleep(2)
    return 10

def main() -> None:

    print(do_action(10, 20))

if __name__ == '__main__':
    main()
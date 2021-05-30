from typing import Any, List, TypeVar, Optional

# def foo(sequence: List[int]) -> None:
#     for i in sequence:
#         print(i )
    
# if __name__ == '__main__':
#     seq: List[Any] = [1, 2, 1.2 ,'4']
#     foo(seq)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        b, a = a + b, b

print([n for n in fib(3.6)])
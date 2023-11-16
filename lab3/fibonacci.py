import timeit
from functools import lru_cache


def fibonacci(n):
    if n <= 0:
        return "n musi byc dodatnie"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache()
def fibonacci2(n):
    if n <= 0:
        return "n musi byc dodatnie"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


if __name__ == '__main__':

    for i in range(1, 11):
        print(f"F({i}) = {fibonacci(i)}")

    time1 = timeit.timeit("fibonacci(20)", setup="from __main__ import fibonacci", number=1000)
    print(f"Czas dla normalnej funkcji: {time1}")

    time2 = timeit.timeit("fibonacci2(20)", setup="from __main__ import fibonacci2", number=1000)
    print(f"Czas dla funkcji z dekoratorem @lru_cache(): {time2}")

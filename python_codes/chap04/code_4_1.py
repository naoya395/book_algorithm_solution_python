def func(n: int) -> int:
    if n == 0:
        return 0
    return n + func(n - 1)

memo: list[int] = []


def fibo(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    if memo[n] != -1:
        return memo[n]

    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


def main() -> None:
    global memo
    memo = [-1] * 50

    fibo(49)

    for n in range(2, 50):
        print(f"{n} 項目: {memo[n]}")


if __name__ == "__main__":
    main()

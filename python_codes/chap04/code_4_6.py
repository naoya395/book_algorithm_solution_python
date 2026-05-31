def fibo(n: int) -> int:
    print(f"fibo({n}) を呼び出しました")

    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibo(n - 1) + fibo(n - 2)
    print(f"{n} 項目 = {result}")

    return result


def main() -> None:
    fibo(6)


if __name__ == "__main__":
    main()

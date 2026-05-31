def func(n: int) -> int:
    print(f"func({n}) を呼び出しました")

    if n == 0:
        return 0

    result = n + func(n - 1)
    print(f"{n} までの和 = {result}")

    return result


def main() -> None:
    func(5)


if __name__ == "__main__":
    main()

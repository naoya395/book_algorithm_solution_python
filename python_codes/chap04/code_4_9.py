def func(i: int, w: int, a: list[int]) -> bool:
    if i == 0:
        if w == 0:
            return True
        return False

    if func(i - 1, w, a):
        return True

    if func(i - 1, w - a[i - 1], a):
        return True

    return False


def main() -> None:
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    if func(n, w, a):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

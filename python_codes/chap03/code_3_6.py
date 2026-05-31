def main() -> None:
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    exist = False
    for bit in range(1 << n):
        total = 0
        for i in range(n):
            if bit & (1 << i):
                total += a[i]

        if total == w:
            exist = True

    if exist:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

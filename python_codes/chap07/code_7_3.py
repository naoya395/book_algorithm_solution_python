def main() -> None:
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    total = 0
    for i in range(n - 1, -1, -1):
        a[i] += total
        amari = a[i] % b[i]
        d = 0
        if amari != 0:
            d = b[i] - amari
        total += d

    print(total)


if __name__ == "__main__":
    main()

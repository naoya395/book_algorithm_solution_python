INF = 20000000


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_value = INF
    for i in range(n):
        for j in range(n):
            if a[i] + b[j] < k:
                continue

            if a[i] + b[j] < min_value:
                min_value = a[i] + b[j]

    print(min_value)


if __name__ == "__main__":
    main()

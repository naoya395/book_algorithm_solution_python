INF = 20000000


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    min_value = INF
    for i in range(n):
        if a[i] < min_value:
            min_value = a[i]

    print(min_value)


if __name__ == "__main__":
    main()

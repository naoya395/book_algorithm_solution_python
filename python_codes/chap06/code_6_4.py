from bisect import bisect_left

INF = 20000000


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_value = INF

    b.sort()
    b.append(INF)

    for i in range(n):
        index = bisect_left(b, k - a[i])
        val = b[index]

        if a[i] + val < min_value:
            min_value = a[i] + val

    print(min_value)


if __name__ == "__main__":
    main()

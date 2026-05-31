INF = 1 << 60


def chmin(a: int, b: int) -> int:
    if a > b:
        return b
    return a


def main() -> None:
    n = int(input())
    c = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        c[i] = list(map(int, input().split()))

    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(n + 1):
        for j in range(i):
            dp[i] = chmin(dp[i], dp[j] + c[j][i])

    print(dp[n])


if __name__ == "__main__":
    main()

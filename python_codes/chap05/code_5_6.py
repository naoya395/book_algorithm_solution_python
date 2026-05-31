INF = 1 << 60

n = 0
h: list[int] = []
dp: list[int] = []


def chmin(a: int, b: int) -> int:
    if a > b:
        return b
    return a


def rec(i: int) -> int:
    if dp[i] < INF:
        return dp[i]

    if i == 0:
        return 0

    res = INF
    res = chmin(res, rec(i - 1) + abs(h[i] - h[i - 1]))

    if i > 1:
        res = chmin(res, rec(i - 2) + abs(h[i] - h[i - 2]))

    dp[i] = res
    return dp[i]


def main() -> None:
    global n, h, dp
    n = int(input())
    h = list(map(int, input().split()))

    dp = [INF] * n

    print(rec(n - 1))


if __name__ == "__main__":
    main()

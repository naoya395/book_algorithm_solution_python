INF = 1 << 29


def main() -> None:
    s, t = input().split()

    dp = [[INF] * (len(t) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = 0

    for i in range(len(s) + 1):
        for j in range(len(t) + 1):
            if i > 0 and j > 0:
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)

    print(dp[len(s)][len(t)])


if __name__ == "__main__":
    main()

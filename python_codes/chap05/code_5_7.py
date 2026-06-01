def main() -> None:
    n, w = map(int, input().split())
    weight = [0] * n
    value = [0] * n
    for i in range(n):
        weight[i], value[i] = map(int, input().split())

    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(n):
        for weight_sum in range(w + 1):
            if weight_sum - weight[i] >= 0:
                dp[i + 1][weight_sum] = max(
                    dp[i + 1][weight_sum],
                    dp[i][weight_sum - weight[i]] + value[i],
                )

            dp[i + 1][weight_sum] = max(dp[i + 1][weight_sum], dp[i][weight_sum])

    print(dp[n][w])


if __name__ == "__main__":
    main()

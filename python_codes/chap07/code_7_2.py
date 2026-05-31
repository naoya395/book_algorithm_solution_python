def main() -> None:
    n = int(input())
    inter = []
    for _ in range(n):
        start, end = map(int, input().split())
        inter.append((start, end))

    inter.sort(key=lambda interval: interval[1])

    res = 0
    current_end_time = 0
    for i in range(n):
        if inter[i][0] < current_end_time:
            continue

        res += 1
        current_end_time = inter[i][1]

    print(res)


if __name__ == "__main__":
    main()

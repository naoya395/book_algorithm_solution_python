import math


def calc_dist(x1: float, y1: float, x2: float, y2: float) -> float:
    """2 点 (x1, y1) と (x2, y2) の距離を求める関数。"""
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def main() -> None:
    n = int(input())
    x = [0.0] * n
    y = [0.0] * n

    for i in range(n):
        x[i], y[i] = map(float, input().split())

    minimum_dist = 100000000.0

    for i in range(n):
        for j in range(i + 1, n):
            dist_i_j = calc_dist(x[i], y[i], x[j], y[j])
            if dist_i_j < minimum_dist:
                minimum_dist = dist_i_j

    print(minimum_dist)


if __name__ == "__main__":
    main()

def main() -> None:
    n = int(input())
    h = [0] * n
    s = [0] * n
    for i in range(n):
        h[i], s[i] = map(int, input().split())

    m = 0
    for i in range(n):
        m = max(m, h[i] + s[i] * n)

    left = 0
    right = m
    while right - left > 1:
        mid = (left + right) // 2

        ok = True
        t = [0] * n
        for i in range(n):
            if mid < h[i]:
                ok = False
            else:
                t[i] = (mid - h[i]) // s[i]

        t.sort()
        for i in range(n):
            if t[i] < i:
                ok = False

        if ok:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()

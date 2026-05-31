VALUE = [500, 100, 50, 10, 5, 1]


def main() -> None:
    x = int(input())
    a = list(map(int, input().split()))

    result = 0
    for i in range(6):
        add = x // VALUE[i]

        if add > a[i]:
            add = a[i]

        x -= VALUE[i] * add
        result += add

    print(result)


if __name__ == "__main__":
    main()

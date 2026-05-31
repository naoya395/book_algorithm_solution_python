N = 8
A = [3, 5, 8, 10, 14, 17, 21, 39]


def binary_search(key: int) -> int:
    left = 0
    right = len(A) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if A[mid] == key:
            return mid
        if A[mid] > key:
            right = mid - 1
        elif A[mid] < key:
            left = mid + 1
    return -1


def main() -> None:
    print(binary_search(10))
    print(binary_search(3))
    print(binary_search(39))

    print(binary_search(-100))
    print(binary_search(9))
    print(binary_search(100))


if __name__ == "__main__":
    main()

def main() -> None:
    f = [0] * 50
    f[0] = 0
    f[1] = 1
    for n in range(2, 50):
        f[n] = f[n - 1] + f[n - 2]
        print(f"{n} 項目: {f[n]}")


if __name__ == "__main__":
    main()

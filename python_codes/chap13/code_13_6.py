import sys


sys.setrecursionlimit(10 ** 7)

seen: list[bool] = []
order: list[int] = []


def rec(G: list[list[int]], v: int) -> None:
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        rec(G, next_v)

    order.append(v)


def main() -> None:
    global seen, order

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    seen = [False] * N
    order = []
    for v in range(N):
        if seen[v]:
            continue
        rec(G, v)
    order.reverse()

    for v in order:
        print(f"{v} -> ", end="")
    print()


if __name__ == "__main__":
    main()

import sys


sys.setrecursionlimit(10 ** 7)

seen: list[bool] = []


def dfs(G: list[list[int]], v: int) -> None:
    seen[v] = True

    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)


def main() -> None:
    global seen

    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)

    seen = [False] * N
    for v in range(N):
        if seen[v]:
            continue
        dfs(G, v)


if __name__ == "__main__":
    main()

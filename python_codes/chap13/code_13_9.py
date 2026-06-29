import sys


sys.setrecursionlimit(10 ** 7)

depth: list[int] = []
subtree_size: list[int] = []


def dfs(G: list[list[int]], v: int, p: int = -1, d: int = 0) -> None:
    depth[v] = d
    for c in G[v]:
        if c == p:
            continue
        dfs(G, c, v, d + 1)

    subtree_size[v] = 1
    for c in G[v]:
        if c == p:
            continue
        subtree_size[v] += subtree_size[c]


def main() -> None:
    global depth, subtree_size

    N = int(input())

    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    root = 0
    depth = [0] * N
    subtree_size = [0] * N
    dfs(G, root)

    for v in range(N):
        print(f"{v}: depth = {depth[v]}, subtree_size = {subtree_size[v]}")


if __name__ == "__main__":
    main()

import sys


sys.setrecursionlimit(10 ** 7)

color: list[int] = []


def dfs(G: list[list[int]], v: int, cur: int = 0) -> bool:
    color[v] = cur

    for next_v in G[v]:
        if color[next_v] != -1:
            if color[next_v] == cur:
                return False
            continue

        if not dfs(G, next_v, 1 - cur):
            return False

    return True


def main() -> None:
    global color

    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    color = [-1] * N
    is_bipartite = True
    for v in range(N):
        if color[v] != -1:
            continue
        if not dfs(G, v):
            is_bipartite = False

    if is_bipartite:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

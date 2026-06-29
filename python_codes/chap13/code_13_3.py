from collections import deque


def BFS(G: list[list[int]], s: int) -> list[int]:
    N = len(G)
    dist = [-1] * N
    que = deque()

    dist[s] = 0
    que.append(s)

    while que:
        v = que.popleft()

        for x in G[v]:
            if dist[x] != -1:
                continue

            dist[x] = dist[v] + 1
            que.append(x)

    return dist


def main() -> None:
    N, M = map(int, input().split())

    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    dist = BFS(G, 0)

    for v in range(N):
        print(f"{v}: {dist[v]}")


if __name__ == "__main__":
    main()

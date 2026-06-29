from collections import deque


def search(G: list[list[int]], s: int) -> None:
    N = len(G)

    seen = [False] * N
    todo = deque()

    seen[s] = True
    todo.append(s)

    while todo:
        v = todo.popleft()

        for x in G[v]:
            if seen[x]:
                continue

            seen[x] = True
            todo.append(x)

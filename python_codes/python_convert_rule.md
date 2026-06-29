# Python 変換ルール

このリポジトリでは、教科書の C++ サンプルコードを、Python しか書かない人でも読みやすく、かつ C/C++ の試験答案にも戻しやすい形で Python に翻訳する。

方針は「Python の便利機能を使いすぎない、素朴で対応関係が見えるコード」にする。

## 基本方針

- C++ の処理順、変数名、関数分割をなるべく保つ。
- Python らしさより、アルゴリズムの対応関係を優先する。
- 入力を読む処理は、基本的に `main()` にまとめ、末尾で `main()` を呼ぶ。
- `if __name__ == "__main__": main()` は必須にしない。
  - 他のファイルから import して再利用・テストしたいコードでは使ってよい。
  - 大学院入試や手書き答案を意識する場合は、単に `main()` と呼ぶだけでよい。
- 型ヒントは、読みやすい範囲で付ける。
  - 例: `def dfs(G: list[list[int]], v: int) -> None:`
  - 複雑になりすぎる型ヒントは無理に付けない。
- コメントは、C++ の文字化けコメントをそのまま移さない。
  - 必要な箇所だけ、短い日本語コメントに置き換える。
  - 1 行ごとに説明しすぎず、処理のかたまりごとに書く。

## ファイル配置

- C++ の `codes/chapXX/code_XX_Y.cpp` は、Python では `python_codes/chapXX/code_XX_Y.py` に置く。
- 章ごとに `python_codes/chapXX` ディレクトリを作る。
- C++ 側に出力がないコードは、Python 側でも基本的に出力を追加しない。

## 文字コード

- 元の C++ ファイルは、コメントが EUC-JP で書かれている
- C++ のコメントを読むときは、まず EUC-JP として読み込む。
- Python に変換したファイルは UTF-8 で保存する。
- 文字化けしたコメントを見ながら翻訳せず、EUC-JP として正しく読めるコメントを参考にする。

## 入出力

- 入力は原則として `input()` を使う。
  - 例: `N, M = map(int, input().split())`
  - 例: `A = list(map(int, input().split()))`
- 大量入力が明らかに必要な場合だけ、`sys.stdin.readline` を検討する。
- 出力は C++ の `cout` と同じ形式にする。
  - `endl` は `print()` に対応させる。
  - 横に並べる出力は `print(..., end="")` や文字列結合を使い、元の空白や改行を保つ。

## 使う Python 機能の基準

使ってよいもの:

- `list`
- `tuple`
- `range`
- `len`
- `min`, `max`, `abs`
- `sort`, `reverse`
- `collections.deque`
- `heapq`
- 簡単なクラス

なるべく避けるもの:

- 複雑なリスト内包表記
- `lambda`
- `map` や `filter` の多段利用
- `zip`, `enumerate` の多用
- `set`, `dict` を使った過度に Python らしい書き換え
- `any`, `all` によるループの圧縮
- ワンライナー化

ただし、`list(map(int, input().split()))` と `G = [[] for _ in range(N)]` は競技プログラミングの基本形なので使う。

## C++ から Python への対応

- `vector<int>` は `list[int]`。
- `vector<vector<int>>` は `list[list[int]]`。
- `vector<T>(N, value)` は `[value] * N`。
- ただし、二次元配列は `[[value] * W for _ in range(H)]` にする。
- `push_back(x)` は `append(x)`。
- `queue<int>` は `collections.deque`。
  - `push` は `append`
  - `front` と `pop` は `popleft`
- `priority_queue` の最小ヒープは `heapq`。
  - `heappush(que, (dist, v))`
  - `d, v = heappop(que)`
- `reverse(order.begin(), order.end())` は `order.reverse()`。
- `sort(edges.begin(), edges.end())` は `edges.sort()`。
- `bool` は `True` / `False`。
- `long long` 相当の値は Python では普通の `int` でよい。
- `const long long INF = 1LL << 60;` は `INF = 1 << 60`。

## chmin / chmax

C++ の `chmin(a, b)` や `chmax(a, b)` は、Python では関数化せず、基本的に明示的な `if` で書く。

```python
if dist[to] > dist[v] + w:
    dist[to] = dist[v] + w
    update = True
```

単に値を更新するだけでよい場面では、次のように書いてもよい。

```python
res = min(res, value)
```

「更新されたかどうか」を判定に使う場面では、`if` を使って C++ の `chmin` の意味を残す。

## グラフ

単純なグラフは、隣接リストで表す。

```python
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
```

無向グラフでは両方向に追加する。

```python
G[a].append(b)
G[b].append(a)
```

重み付きグラフは、まずはタプル `(to, w)` で表す。

```python
G[a].append((b, w))
for to, w in G[v]:
    ...
```

辺に多くの情報がある場合は、簡単なクラスを使ってよい。

## DFS / 再帰

- C++ の再帰 DFS は、Python でも再帰で書いてよい。
- 深い再帰があり得る章では、先頭付近で `import sys` と `sys.setrecursionlimit(10 ** 7)` を入れる。
- C++ 側で `seen`, `color`, `depth`, `subtree_size` などがグローバルなら、Python 側でもグローバル変数として対応させてよい。
- グローバル変数を `main()` で代入する場合は、`global` を明示する。

```python
seen: list[bool] = []


def dfs(G: list[list[int]], v: int) -> None:
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dfs(G, next_v)
```

## BFS

BFS は `deque` を使う。

```python
from collections import deque

que = deque()
que.append(s)

while que:
    v = que.popleft()
    for next_v in G[v]:
        ...
```

距離配列は、未訪問を `-1` として初期化する。

```python
dist = [-1] * N
dist[s] = 0
```

## クラス

Union-Find や最大流のように、C++ で `struct` を使っているコードは Python でもクラスにする。

- メソッド名は C++ の名前をなるべく保つ。
  - `root`
  - `issame`
  - `unite`
  - `size`
- `__init__` で配列を初期化する。
- `self.par`, `self.siz` のように、C++ のメンバ変数と対応させる。

## chap13 の変換方針

chap13 はグラフ探索が中心なので、C++ の構造をほぼそのまま Python に移す。

- `code_13_2`: DFS。全頂点を始点候補として探索する。元コードに出力がないので、Python でも出力しない。
- `code_13_3`: BFS。`deque` を使い、頂点 0 からの距離を `v: dist[v]` の形式で出力する。
- `code_13_4`: DFS による到達判定。`seen[t]` で `Yes` / `No` を出力する。
- `code_13_5`: 二部グラフ判定。`color = [-1] * N` とし、再帰 DFS で色を 0 / 1 に分ける。
- `code_13_6`: トポロジカルソート。帰りがけ順に `order.append(v)` し、最後に `order.reverse()` する。
- `code_13_9`: 木の DFS。`depth` と `subtree_size` をグローバル配列にし、親 `p` への逆流を避ける。

## chap14 以降の変換方針

chap14 以降では、重み付きグラフ、最短路、Union-Find、最大流が出てくる。

- Bellman-Ford は、`chmin` 関数を作らず、更新判定を `if` で書く。
- Dijkstra の単純版は、C++ と同じく `used` と `dist` を使った二重ループで書く。
- Dijkstra のヒープ版は、`heapq` を使う。
- Floyd-Warshall は三重ループをそのまま書く。
- Kruskal は、辺を `(w, u, v)` のタプルにして `edges.sort()` する。
- Union-Find はクラスで書く。
- 最大流は、C++ の `Graph`, `Edge`, `FordFulkerson` の構造が重要なので、Python でも簡単なクラスで対応させる。

## 確認

変換後は、少なくとも次を確認する。

- `python -m py_compile 対象ファイル.py` が通ること。
- サンプル入力が分かる場合は、C++ と同じ出力形式になっていること。
- 元 C++ の出力がないコードでは、Python 側でも余計な出力を足していないこと。

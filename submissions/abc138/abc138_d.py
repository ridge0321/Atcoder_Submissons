import sys

sys.setrecursionlimit(1000000)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N - 1)]
PX = [list(map(int, input().split())) for i in range(Q)]

tree_dict = {}
tree_counta = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(1, N + 1):
    tree_dict[i] = []

for ab in AB:
    a = ab[0]
    b = ab[1]
    tree_dict[a].append(b)
    tree_dict[b].append(a)

for px in PX:
    p = px[0]
    x = px[1]
    tree_counta[p] += x


def bfs(now, prev_count):
    visited[now] = True
    tree_counta[now] += prev_count

    for next_node in tree_dict[now]:
        if not visited[next_node]:
            bfs(next_node, tree_counta[now])


bfs(1, 0)

print(*tree_counta[1:])

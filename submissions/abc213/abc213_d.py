# 再起回数上限を10^6へ変更
import sys

sys.setrecursionlimit(10**6)

N = int(input())

road_dict = {}
visited = [False] * (N + 1)
visited[1] = True
start = 1
stack = []

for i in range(1, N + 1):
    road_dict[i] = []

for i in range(N - 1):
    A, B = map(int, input().split())
    road_dict[A].append(B)
    road_dict[B].append(A)

for i in range(1, N + 1):
    road_dict[i].sort()


def DFS(now):
    stack.append(now)
    visited[now] = True
    for next_city in road_dict[now]:
        if not visited[next_city]:
            DFS(next_city)
            stack.append(now)


DFS(start)

print(*stack)
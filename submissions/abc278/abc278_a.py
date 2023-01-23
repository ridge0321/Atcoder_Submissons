from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
que = deque(A)

for i in range(K):
    que.popleft()
    que.append(0)

print(*list(que))

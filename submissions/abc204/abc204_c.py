from collections import deque

N, M = map(int, input().split())
road_dict = {}
for i in range(1, N + 1):
    road_dict[i] = []

for _ in range(M):
    A, B = map(int, input().split())
    road_dict[A].append(B)

# print(road_dict)


def BFS(start):
    visited = [False] * (N + 1)
    que = deque()
    visited[start] = True
    visit_count = 0
    que.append(start)

    while len(que) > 0:
        now_city = que.popleft()
        visit_count += 1

        for next_city in road_dict[now_city]:
            if visited[next_city] == False:
                que.append(next_city)
                visited[next_city] = True

    return visit_count


ans = 0
for i in range(1, N + 1):
    ans += BFS(i)

print(ans)

from collections import deque

N, M = map(int, input().split())

road_dict = {}
city_infor = {}
que = deque()
visited = [False] * (N + 1)

inf = 10**15
mod = 10**9 + 7

for i in range(1, N + 1):
    city_infor[i] = [0, 0]
    road_dict[i] = []

for i in range(M):
    A, B = map(int, input().split())
    road_dict[A].append(B)
    road_dict[B].append(A)

for i in range(1, N + 1):
    road_dict[i].sort()


visited[1] = True
time = 1
root = 1
que.append(1)

city_infor[1][0] = 1
city_infor[1][1] = 1


while len(que) > 0:

    now = que.popleft()

    for next in road_dict[now]:
        if not visited[next]:
            visited[next] = True
            que.append(next)
            city_infor[next][0] = city_infor[now][0]
            city_infor[next][1] = city_infor[now][1] + 1

            city_infor[next][0] %= mod

        else:
            if city_infor[next][1] == city_infor[now][1] + 1:
                city_infor[next][0] += city_infor[now][0]

if visited[N]:
    print(city_infor[N][0] % mod)
else:
    print(0)

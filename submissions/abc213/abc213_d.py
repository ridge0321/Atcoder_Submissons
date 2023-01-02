import sys

# import copy

sys.setrecursionlimit(1000000)
N = int(input())
AB = [list(map(int, input().split())) for i in range(N - 1)]

travel_log = []

road_dict = {}


def dfs(now, prev):
    travel_log.append(now)

    for next_town in road_dict[now]:
        if not next_town == prev:

            dfs(next_town, now)
            travel_log.append(now)


for i in range(1, N + 1):
    road_dict[i] = []

for ab in AB:
    a = ab[0]
    b = ab[1]
    road_dict[a].append(b)
    road_dict[b].append(a)

for k in road_dict.keys():
    road_dict[k].sort()

dfs(1, -1)

print(*travel_log)

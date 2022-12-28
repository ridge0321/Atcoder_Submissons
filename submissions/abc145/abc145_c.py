import itertools
import math

N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]

l = []
for i in range(N):
    l.append(i)
# print(l)

permutation = list(map(list, itertools.permutations(l, N)))
# print(permutation)
distance_list = []

for root in permutation:
    # print(root)
    for i in range(N - 1):
        this_city = root[i]
        next_city = root[i + 1]

        this_x = XY[this_city][0]
        this_y = XY[this_city][1]

        next_x = XY[next_city][0]
        next_y = XY[next_city][1]

        distance = ((next_x - this_x) ** 2 + (next_y - this_y) ** 2) ** 0.5
        distance_list.append(distance)


print(sum(distance_list) / math.factorial(N))

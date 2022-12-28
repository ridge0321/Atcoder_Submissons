import itertools

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for i in range(M)]

num = [i for i in range(N)]

p_list = list(map(list, itertools.permutations(num)))

# print(p_list)
# print(len(p_list))

xy_dict = {}
for i in range(1, N + 1):
    xy_dict[i] = []

for xy in XY:
    x = xy[0]
    y = xy[1]
    xy_dict[x].append(y)
    xy_dict[y].append(x)

# print(xy_dict)


first_p = True
p_list_min = -1

for p in p_list:
    p_sum = 0
    # 最初
    if first_p:
        for i in range(N - 1):
            if p[i + 1] + 1 in xy_dict[p[i] + 1]:
                break
        else:
            for i in range(N):
                p_sum += A[p[i]][i]
            p_list_min = p_sum
            first_p = False

    #  二回目以降
    else:
        for i in range(N - 1):
            if p[i + 1] + 1 in xy_dict[p[i] + 1]:
                break
        else:
            for i in range(N):
                # 走者p[i]は区間iを走る
                p_sum += A[p[i]][i]
            p_list_min = min(p_list_min, p_sum)


print(p_list_min)

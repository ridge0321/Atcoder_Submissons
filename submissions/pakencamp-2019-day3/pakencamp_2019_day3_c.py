N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

index_list = list(range(M))
c_list = []
sum_point_list = []

for i in range(M - 1):
    for j in range(i + 1, M):
        c_list.append([i, j])

for c in c_list:
    t1 = c[0]
    t2 = c[1]
    sum_point = 0
    for i in range(N):
        sum_point += max(A[i][t1], A[i][t2])
    sum_point_list.append(sum_point)

print(max(sum_point_list))

N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for i in range(M)]

t_sum = sum(T)

for px in PX:
    pi = px[0]
    xi = px[1]
    print(t_sum - T[pi - 1] + xi)

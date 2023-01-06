N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]


def distance(i, j):
    xi = XY[i][0]
    yi = XY[i][1]
    xj = XY[j][0]
    yj = XY[j][1]

    dis = ((xi - xj) ** 2 + (yi - yj) ** 2) ** (0.5)
    return dis


ans_l = []

for i in range(N - 1):
    for j in range(i + 1, N):
        ans_l.append(distance(i, j))

print(max(ans_l))

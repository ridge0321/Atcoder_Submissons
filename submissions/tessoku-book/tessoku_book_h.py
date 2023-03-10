H, W = map(int, input().split())

X = [[0] * (W + 1) for _ in range(H + 1)]
cum = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(1, H + 1):
    x_row = list(map(int, input().split()))

    for j in range(1, W + 1):
        X[i][j] = x_row[j - 1]


for i in range(1, H + 1):
    for j in range(1, W + 1):
        cum[i][j] = cum[i][j - 1] + X[i][j]


for j in range(1, W + 1):
    for i in range(1, H + 1):
        cum[i][j] += cum[i - 1][j]


Q = int(input())

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = cum[C][D] - (cum[C][B - 1] + cum[A - 1][D]) + cum[A - 1][B - 1]

    print(ans)

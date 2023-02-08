N = int(input())
X, Y = map(int, input().split())

inf = 10**10

dp = [[[inf] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N + 1):
    A, B = map(int, input().split())
    for x in range(X + 1):
        for y in range(Y + 1):
            dp[i][x][y] = min(dp[i - 1][x][y], dp[i][x][y])
            x_p = min(X, x + A)
            y_p = min(Y, y + B)

            dp[i][x_p][y_p] = min(dp[i - 1][x][y] + 1, dp[i][x_p][y_p])

ans = dp[N][X][Y]

if ans >= inf:
    print(-1)
else:
    print(ans)

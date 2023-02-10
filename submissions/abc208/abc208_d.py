N, M = map(int, input().split())

inf = 10**15

dp = [[[inf] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(M):
    A, B, C = map(int, input().split())
    dp[0][A][B] = C

for i in range(1, N + 1):
    dp[0][i][i] = 0

for k in range(1, N + 1):
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            old = dp[k - 1][s][t]
            new = dp[k - 1][s][k] + dp[k - 1][k][t]

            dp[k][s][t] = min(old, new)

ans = 0
for k in range(1, N + 1):
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            if dp[k][s][t] < inf:
                ans += dp[k][s][t]

print(ans)

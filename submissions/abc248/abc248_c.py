N, M, K = map(int, input().split())

dp = [[0] * (K + 1) for i in range(N + 1)]
mod = 998244353

for i in range(1, M + 1):
    dp[1][i] = 1

for i in range(2, len(dp)):
    for j in range(1, len(dp[i])):
        for k in range(1, j):
            if j - k <= M:
                dp[i][j] += dp[i - 1][k]
    dp[i][j] %= mod

ans = 0
for i in range(1, K + 1):
    ans += dp[len(dp) - 1][i]
    ans %= mod
print(ans)

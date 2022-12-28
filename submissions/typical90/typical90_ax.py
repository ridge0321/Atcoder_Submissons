N, L = map(int, input().split())

dp = [0] * (N + L + 1)
dp[1] = 1
dp[L] = 1

for i in range(1, N + 1):
    dp[i + 1] += dp[i]
    dp[i + L] += dp[i]
print(dp[N] % (10**9 + 7))

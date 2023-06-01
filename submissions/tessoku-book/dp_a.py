N = int(input())
h = [0] + list(map(int, input().split())) + [10**10] * 10

dp = [10**10] * (N + 10)

dp[0] = 0
dp[1] = 0


for i in range(1, N + 1):
    dp[i + 1] = min(dp[i] + abs(h[i] - h[i + 1]), dp[i + 1])
    dp[i + 2] = min(dp[i] + abs(h[i] - h[i + 2]), dp[i + 2])

print(dp[N])

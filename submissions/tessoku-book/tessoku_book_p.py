N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

dp = [10**6] * (N + 1)
dp[0] = 0
dp[1] = 0
dp[2] = A[1]

for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i - 1], B[i - 2] + dp[i - 2])

print(dp[N])

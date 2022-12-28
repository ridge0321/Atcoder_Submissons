X = int(input())
loop_limit = X // 105 + 1

dp = [False] * (X + 106)
dp[0] = True
# print(len(dp))

for i in range(0, X + 1):
    if dp[i]:
        dp[i + 100] = True
        dp[i + 101] = True
        dp[i + 102] = True
        dp[i + 103] = True
        dp[i + 104] = True
        dp[i + 105] = True

if dp[X]:
    print(1)
else:
    print(0)

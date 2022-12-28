X, Y = map(int, input().split())

dp = [X]
for i in range(Y):
    next = dp[i] * 2
    if next > Y:
        break
    else:
        dp.append(next)

print(len(dp))

N = int(input())
h = [0] + list(map(int, input().split())) + [10**10] * 10


dp = [10**10] * (N + 10)

dp[0] = 0
dp[1] = 0


for i in range(1, N + 1):
    dp[i + 1] = min(dp[i] + abs(h[i] - h[i + 1]), dp[i + 1])
    dp[i + 2] = min(dp[i] + abs(h[i] - h[i + 2]), dp[i + 2])

# print(dp[N])

index = N
root = [N]
while index > 2:
    if abs(h[index] - h[index - 1]) == dp[index] - dp[index - 1]:
        root.append(index - 1)
        index -= 1
    else:
        root.append(index - 2)
        index -= 2

if index == 2:
    root.append(1)

print(len(root))
print(*reversed(root))

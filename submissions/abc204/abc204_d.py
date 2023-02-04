N = int(input())
T = [0] + list(map(int, input().split()))

T_sum = sum(T)
dp = [[False] * (T_sum + 1) for i in range(N + 1)]
dp[0][0] = True


for i in range(1, N + 1):
    for j in range(T_sum + 1):

        if dp[i - 1][j]:
            dp[i][j] = True

        if dp[i - 1][j - T[i]] == True and j - T[i] >= 0:
            dp[i][j] = True

ans = []
for i in range(sum(T) + 1):
    if dp[N][i]:
        ans.append(max(i, T_sum - i))

# print(ans)
print(min(ans))


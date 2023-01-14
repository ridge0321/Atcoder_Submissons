S = list("?" + str(input()))
mod = 10**9 + 7
chokudai_l = list("?chokudai")

dp = [[0] * 9 for i in range(len(S))]

for i in range(len(S)):
    dp[i][0] = 1


for i in range(1, len(S)):
    for j in range(1, 9):

        if S[i] == chokudai_l[j]:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]

        dp[i][j] %= mod

print(dp[len(S) - 1][8])
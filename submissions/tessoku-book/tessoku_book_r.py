N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (10001) for _ in range(N)]


dp[0][0] = True

dp[0][A[0]] = True

for n in range(N):
    dp[n][A[n]] = True
    for s in range(S + 1):
        if dp[n - 1][s]:
            # 引継ぎ
            dp[n][s] = True
            # 追加
            if A[n] + s < 10001:
                dp[n][A[n] + s] = True


# print(dp)
# print(dp[N - 1][S])
if dp[N - 1][S]:
    print("Yes")
else:
    print("No")

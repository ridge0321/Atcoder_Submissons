N, K = map(int, input().split())
S = list(str(input()))

countdown = K
ans_list = []
for i in range(N):
    if countdown <= 0:
        ans_list.append("x")
    else:
        if S[i] == "o":
            countdown -= 1
            ans_list.append("o")
        else:
            ans_list.append("x")

ans = ""
for a in ans_list:
    ans += a
print(ans)

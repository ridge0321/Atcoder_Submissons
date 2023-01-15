S = list(str(input()))

re_s = list(reversed(S))
ans_l = []
for i in range(len(re_s)):
    ans_l.append(ord(re_s[i]) - 64)

ans = 0
for i in range(len(ans_l)):
    ans += ans_l[i] * 26**i

print(ans)

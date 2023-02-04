N, K = map(int, input().split())
S = [str(input()) for i in range(N)]
ans = []
for i in range(K):
    ans.append(S[i])

ans.sort()

for a in ans:
    print(a)

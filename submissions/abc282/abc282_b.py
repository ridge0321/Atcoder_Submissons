N, M = map(int, input().split())
S = [list(str(input())) for i in range(N)]

# print(S)
count = 0
for i in range(len(S) - 1):
    for j in range(i + 1, len(S)):
        # print(S[i], S[j])
        # print(i, j)
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":

                break
        else:
            count += 1

print(count)

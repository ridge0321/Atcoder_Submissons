N = int(input())
S = list(str(input()))

for i in range(1, N):
    l = 0
    for j in range(N):
        if i + j >= N:
            break
        if not (S[j] == S[j + i]):
            l += 1
        else:
            break
    print(l)

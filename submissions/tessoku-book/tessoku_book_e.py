N, K = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j > K - 1:
            break
        elif K - (i + j) <= N and 0 < K - (i + j):
            cnt += 1

print(cnt)

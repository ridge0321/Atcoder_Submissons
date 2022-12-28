N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(M)]

ab_dict = {}

for i in range(1, N + 1):
    ab_dict[i] = 0

for i in range(M):
    a = ab[i][0]
    b = ab[i][1]
    if a > b:
        ab_dict[a] += 1
    else:
        ab_dict[b] += 1

count = 0
for i in range(1, N + 1):
    if ab_dict[i] == 1:
        count += 1

print(count)

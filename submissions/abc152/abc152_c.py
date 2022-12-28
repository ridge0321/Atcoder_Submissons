N = int(input())
P = list(map(int, input().split()))

min_log = []
min_p = P[0]
count = 1

for p in P:
    min_p = min(p, min_p)
    min_log.append(min_p)

# print(min_log)

for i in range(1, N):
    if P[i] < min_log[i - 1]:
        count += 1

print(count)

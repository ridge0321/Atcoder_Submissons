N = int(input())
H = list(map(int, input().split()))

count_log = []
count = 0
for i in range(1, N):
    if H[i] - H[i - 1] > 0:
        count_log.append(count)
        count = 0
    else:
        count += 1
else:
    count_log.append(count)

print(max(count_log))

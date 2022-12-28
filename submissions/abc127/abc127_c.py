N, M = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(M)]

L = []
R = []
count = 0

for lr in LR:
    L.append(lr[0])
    R.append(lr[1])

max_l = max(L)
min_r = min(R)

# print(max(L), min(R))

if max_l > min_r:
    print(0)
else:
    print(min_r - max_l + 1)

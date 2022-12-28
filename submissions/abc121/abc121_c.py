N, M = map(int, input().split())
AB = sorted([list(map(int, input().split())) for i in range(N)])

need = M
cost = 0
# print(AB)
for ab in AB:
    if ab[1] < need:
        need -= ab[1]
        cost += ab[0] * ab[1]
    elif ab[1] >= need:
        cost += ab[0] * need
        need = 0

print(cost)

N, W = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

AB.sort(reverse=True)
cheese_w = 0
yummy = 0
for ab in AB:
    if W < cheese_w:
        break

    a = ab[0]
    b = ab[1]

    if b + cheese_w <= W:
        cheese_w += b
        yummy += a * b
    else:
        yummy += a * (W - cheese_w)
        break

print(yummy)

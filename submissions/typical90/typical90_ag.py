H, W = map(int, input().split())

if H == 1 or W == 1:
    ans = H * W
else:

    if W % 2 == 0:
        row_light = W // 2
    else:
        row_light = W // 2 + 1

    if H % 2 == 0:
        ans = row_light * H // 2
    else:
        ans = row_light * (H // 2 + 1)

print(ans)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]

ans = "Yes"
count = 0
for i in range(H - 1):
    for j in range(W - 1):
        target = B[i][j]

        xy = A[i][j]
        xy_right = A[i][j + 1]
        xy_under = A[i + 1][j]
        xy_r_u = A[i + 1][j + 1]

        differ = target - xy
        count += abs(differ)

        xy += differ
        xy_right += differ
        xy_under += differ
        xy_r_u += differ

        A[i][j] = xy
        A[i][j + 1] = xy_right
        A[i + 1][j] = xy_under
        A[i + 1][j + 1] = xy_r_u

    else:
        if not (A[i][W - 1] == B[i][W - 1]):
            ans = "No"
            break
else:
    for j in range(W):
        if not (A[H - 1][j] == B[H - 1][j]):
            ans = "No"
            break

print(ans)
if ans == "Yes":
    print(count)

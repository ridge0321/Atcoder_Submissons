N = int(input())
H = list(map(int, input().split()))

for i in range(1, N):
    this_h = H[i]
    prev_h = H[i - 1]

    if this_h < prev_h:
        ans = "No"
        break
    elif this_h > prev_h:
        H[i] -= 1
else:
    ans = "Yes"
print(ans)

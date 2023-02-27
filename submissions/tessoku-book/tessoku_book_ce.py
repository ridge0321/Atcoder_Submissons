N = int(input())
A = list(map(int, input().split()))
Q = int(input())

cum = [0]
for i in range(len(A)):
    cum.append(cum[i] + A[i])

# print(cum)

for _ in range(Q):
    L, R = map(int, input().split())
    sec_num = R - L + 1
    result = cum[R] - cum[L - 1]

    # print(result)

    if sec_num == result * 2:
        ans = "draw"
    elif sec_num > result * 2:
        ans = "lose"
    else:
        ans = "win"

    print(ans)

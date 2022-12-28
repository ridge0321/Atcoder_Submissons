N = int(input())
CP = [list(map(int, input().split())) for i in range(N)]

Q = int(input())
LR = [list(map(int, input().split())) for i in range(Q)]

cum_sum_1 = []
cum_sum_2 = []

if CP[0][0] == 1:
    cum_sum_1.append(CP[0][1])
    cum_sum_2.append(0)
else:
    cum_sum_2.append(CP[0][1])
    cum_sum_1.append(0)

for i in range(1, N):
    # pre_cp = CP[i-1]
    cp = CP[i]

    if cp[0] == 1:
        cum_sum_1.append(cum_sum_1[i - 1] + cp[1])
        cum_sum_2.append(cum_sum_2[i - 1])
    else:
        cum_sum_1.append(cum_sum_1[i - 1])
        cum_sum_2.append(cum_sum_2[i - 1] + cp[1])

# print(cum_sum_1)
# print(cum_sum_2)

for lr in LR:
    l = lr[0] - 2
    r = lr[1] - 1
    if l < 0:
        sum_1 = cum_sum_1[r] - 0
        sum_2 = cum_sum_2[r] - 0
    else:
        cum_sum_1[r]
        cum_sum_1[l]
        cum_sum_2[r]
        cum_sum_2[l]

        sum_1 = cum_sum_1[r] - cum_sum_1[l]
        sum_2 = cum_sum_2[r] - cum_sum_2[l]

    print("%d %d" % (sum_1, sum_2))

H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = []

aw_sum = []
ah_sum = []

for i in range(H):

    aw_sum.append(sum(A[i]))

for i in range(W):
    ah = 0
    for j in range(H):
        ah += A[j][i]

    ah_sum.append(ah)

# print(aw_sum)
# print(ah_sum)
for i in range(H):
    bw = []
    for j in range(W):
        bw.append(aw_sum[i] + ah_sum[j] - A[i][j])
    B.append(bw)


for b in B:
    for i in range(len(b)):
        if i == len(b) - 1:
            print("%d" % (b[i]))
        else:
            print("%d " % (b[i]), end="")

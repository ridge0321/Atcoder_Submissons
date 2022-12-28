N, M = map(int, input().split())
KA = [list(map(int, input().split())) for i in range(N)]

A = []
K = []
count = 0
for ka in KA:
    K.append(ka[0])
    A.append(ka[1 : len(ka)])

# print(K)
# print(A)

min_K_index = K.index(min(K))

for an in A[min_K_index]:
    for a_array in A:
        if an not in a_array:
            break
    else:
        count += 1

print(count)
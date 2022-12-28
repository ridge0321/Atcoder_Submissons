# import itertools

# # import math
# import numpy as np

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for i in range(0, N - 4):

    for j in range(i + 1, N - 3):

        for k in range(j + 1, N - 2):

            for l in range(k + 1, N - 1):

                for m in range(l + 1, N):

                    multi = A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P
                    if multi == Q:
                        count += 1


# c_list = list(map(list, itertools.combinations(A, 5)))

# for c in c_list:
#     multi = np.prod(c)
#     if multi % P == Q:
#         count += 1


print(count)

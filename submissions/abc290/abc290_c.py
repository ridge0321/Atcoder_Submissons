N, K = map(int, input().split())
A = list(map(int, input().split()))
set_A = list(set(A))
set_A.sort()

B = set_A[:K] + [0, 0, 0, 0, 0, 0, 0]
# print(B)
# ans = 0
for i in range(K):
    if not (B[i] == i):
        print(i)
        quit()
    # ans = i
else:
    print(B[K - 1] + 1)


# for i in range(0, K):
#     for j in range(0, K):
#         if B[j] == i:
#             break
#     else:
#         print(i)
#         quit()

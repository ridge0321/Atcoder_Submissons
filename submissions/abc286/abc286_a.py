N, P, Q, R, S = map(int, input().split())

A = list(map(int, input().split()))

# if len(A[0 : P - 1]) > 0:
#     print(*A[0 : P - 1], " ", end="")
# if len(A[R - 1 : S]) > 0:
#     print(*A[R - 1 : S], " ", end="")
# if len(A[Q : R - 1]) > 0:
#     print(*A[Q : R - 1], " ", end="")
# if len(A[P - 1 : Q]) > 0:
#     print(*A[P - 1 : Q], " ", end="")
# if len(A[S:]) > 0:
#     print(*A[S:])
# + *A[R-1:S] +

B = []
for b in A[0 : P - 1]:
    B.append(b)
for b in A[R - 1 : S]:
    B.append(b)
for b in A[Q : R - 1]:
    B.append(b)
for b in A[P - 1 : Q]:
    B.append(b)
for b in A[S:]:
    B.append(b)

print(*B)

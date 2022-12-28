N = int(input())
A = list(map(int, input().split()))
Q = int(input())
query = [list(map(int, input().split())) for i in range(Q)]

for i in range(Q):
    if len(query[i]) == 3:
        A[query[i][1] - 1] = query[i][2]
    else:
        print(A[query[i][1] - 1])

n, q = map(int,input().split())

A = list(map(int, input().split()))

shift = 0
for i in range(q):
    t, x, y = map(int,input().split())
    num_x = (x - shift - 1) % n
    num_y = (y - shift - 1) % n
    if t == 1:
        tmp = A[num_x]
        A[num_x] = A[num_y]
        A[num_y] = tmp
    elif t == 2:
        shift += 1
    elif t == 3:
        print(A[num_x])
A, B, C = map(int, input().split())

if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
    print(min(A * B, B * C, C * A))
else:
    print(0)

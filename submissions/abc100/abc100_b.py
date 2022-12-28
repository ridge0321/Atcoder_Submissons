D, N = map(int, input().split())

if D == 0 and N == 100:
    print(101)
elif D == 1 and N == 100:
    print(10100)
elif D == 2 and N == 100:
    print(1010000)
else:
    print(100**D * N)

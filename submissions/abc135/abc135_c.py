N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

monster_sum = sum(a)

for i in range(N):

    if b[i] - a[i] >= 0:
        b[i] = b[i] - a[i]
        a[i] = 0

        if b[i] - a[i + 1] >= 0:
            a[i + 1] = 0
        else:
            a[i + 1] = a[i + 1] - b[i]
    else:
        a[i] = a[i] - b[i]

dead_sum = monster_sum - sum(a)
print(dead_sum)

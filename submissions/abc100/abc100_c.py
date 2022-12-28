N = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(N):
    ai = a[i]
    for j in range(a[i]):
        if ai % 2 == 0:
            ai /= 2
            count += 1
        else:
            break

print(count)

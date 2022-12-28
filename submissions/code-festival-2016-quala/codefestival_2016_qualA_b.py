N = int(input())
a = list(map(int, input().split()))
a.insert(0, -1)
matching = []

count = 0
for i in range(1, N + 1):
    if i == a[a[i]]:
        count += 1
print(int(count / 2))

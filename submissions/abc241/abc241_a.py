a = list(map(int, input().split()))

next_index = 0
for i in range(2):
    next_index = a[next_index]

print(a[next_index])

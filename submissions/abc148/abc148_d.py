N = int(input())
a = list(map(int, input().split()))

pre_index = -1
index_list = []
count = 0
next = 1

if 1 not in a:
    print(-1)
    quit()


for i in range(N):
    if a[i] == next:
        next += 1
    else:
        count += 1

print(count)
N = int(input())
a = list(map(int, input().split()))

max_mod_list = []
for i in range(N):
    max_mod_list.append(a[i] - 1)

print(sum(max_mod_list))

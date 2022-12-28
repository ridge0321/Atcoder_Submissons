import copy

N = int(input())
A = [int(input()) for i in range(N)]

a_copy = copy.deepcopy(A)
max_first = max(a_copy)
a_copy.remove(max_first)
max_second = max(a_copy)

for a in A:
    if a == max_first:
        print(max_second)
    else:
        print(max_first)

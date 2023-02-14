from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

comb_list = list(map(list, combinations(A, 3)))

for comb in comb_list:
    if sum(comb) == 1000:
        print("Yes")
        quit()
else:
    print("No")

    
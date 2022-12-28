import itertools
from itertools import product

N = int(input())
if N % 2 == 1:
    print("")
    quit()

left = ["("] * int(N / 2)
right = [")"] * int(N / 2)

base_list = left + right
# print(base_list)

c_list = list(itertools.combinations(base_list, len(base_list)))

# print(c_list)

ans_list = []
# ( = 1 , ) = -1
for pro in product((-1, 1), repeat=N):
    pro_list = list(pro)
    if sum(pro_list) == 0:
        cum_sum = 0
        correct = True

        for i in range(0, N):
            cum_sum += pro_list[i]
            if cum_sum < 0:
                correct = False

        if correct:

            replace_list = [s.replace("-1", ")") for s in list(map(str, pro_list))]
            replace_list = [s.replace("1", "(") for s in replace_list]

            ans_list.append(replace_list)

# print(ans_list)


for l in reversed(ans_list):
    print("".join(l))

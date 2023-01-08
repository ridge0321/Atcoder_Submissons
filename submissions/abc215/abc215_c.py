import itertools

s, k = map(str, input().split())

s = list(s)
k = int(k)
per_iter = list(itertools.permutations(range(0, len(s))))
s_set = set()
# print(per_iter)

for per in per_iter:
    temp_array = []
    for p_index in per:
        temp_array.append(s[p_index])
    result = "".join(temp_array)
    s_set.add(result)


s_list = list(s_set)
s_list.sort()

print(s_list[k - 1])

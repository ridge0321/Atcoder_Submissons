N = int(input())
S = [str(input()) for i in range(N)]

s_dict = {}

for s in S:
    if s not in s_dict:
        s_dict[s] = 1
    else:
        s_dict[s] += 1

max_count = max(list(s_dict.values()))
# print(max_count)

set_s = sorted(list(set(S)))
for s in set_s:
    if s_dict[s] == max_count:
        print(s)

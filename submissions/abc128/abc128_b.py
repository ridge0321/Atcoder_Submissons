N = int(input())
SP = [list(input().split()) for i in range(N)]

sp_dict = {}

# indexを追加
for i in range(N):
    SP[i].append(i + 1)
    SP[i][1] = int(SP[i][1])

# dictで整理
for sp in SP:
    if sp[0] not in sp_dict:
        sp_dict[sp[0]] = [sp[1:3]]
    else:
        sp_dict[sp[0]].append(sp[1:3])

s_list = sorted(list(sp_dict.keys()))

for s in s_list:
    p_list = sp_dict[s]
    for p in sorted(p_list, reverse=True):
        print(p[1])

# print(s_list)
# print(sp_dict)

S = list(str(input()))

s_dict = {"N": 0, "S": 0, "W": 0, "E": 0}

for s in S:
    s_dict[s] += 1
ans = "Yes"
for s in s_dict:
    # print(s)
    if s_dict[s] == 0:
        n_judge = s == "N" and not (s_dict["S"] == 0)
        s_judge = s == "S" and not (s_dict["N"] == 0)
        w_judge = s == "W" and not (s_dict["E"] == 0)
        e_judge = s == "E" and not (s_dict["W"] == 0)

        if n_judge or s_judge or w_judge or e_judge:
            ans = "No"

print(ans)

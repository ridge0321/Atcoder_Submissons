S = list(str(input()))


f_b_count = 0
f_w_count = 0

for i in range(len(S)):
    if i % 2 == 0 and S[i] == "1":
        f_b_count += 1
    elif i % 2 == 1 and S[i] == "0":
        f_b_count += 1

    if i % 2 == 0 and S[i] == "0":
        f_w_count += 1
    elif i % 2 == 1 and S[i] == "1":
        f_w_count += 1


print(min(f_b_count, f_w_count))

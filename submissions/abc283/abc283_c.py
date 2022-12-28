S = list(str(input()))
zero_flag = 0
count = 0
for i in range(len(S)):
    if S[i] == "0" and zero_flag == 0:
        count += 1
        zero_flag = 1
    elif not (S[i] == "0") and zero_flag == 1:
        count += 1
        zero_flag = 0
    elif S[i] == "0" and zero_flag == 1:
        zero_flag = 0
    else:
        count += 1

print(count)

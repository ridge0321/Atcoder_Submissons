N = int(input())
S = list(str(input()))

all_comb = N * (N + 1) // 2
sum_consec = 0

prev_flag = S[0]
count = 0
for i in range(len(S)):
    if S[i] == prev_flag:
        count += 1
    else:
        consec_count_comb = count * (count + 1) // 2
        sum_consec += consec_count_comb
        count = 1
        prev_flag = S[i]
else:
    consec_count_comb = count * (count + 1) // 2
    sum_consec += consec_count_comb

result = all_comb - sum_consec
print(result)

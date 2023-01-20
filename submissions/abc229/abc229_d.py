S = list(str("_" + input()))
K = int(input())

dot_cum_sum = [0] * len(S)
x_count = 0
x_max = 0

for i in range(1, len(dot_cum_sum)):
    if S[i] == "X":
        x_count += 1
        dot_cum_sum[i] = dot_cum_sum[i - 1]

    elif S[i] == ".":
        dot_cum_sum[i] = dot_cum_sum[i - 1] + 1

r = 1
for l in range(1, len(dot_cum_sum)):
    while r < len(dot_cum_sum):
        sec_len = r - (l - 1)
        sec_dot_count = dot_cum_sum[r] - dot_cum_sum[l - 1]
        r += 1

        if sec_dot_count > K:
            break
        else:
            x_max = max(x_max, sec_len)

print(x_max)

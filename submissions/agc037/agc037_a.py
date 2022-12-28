S = str(input())

count = 1
prev_s = S[0:1]
start_point = 1
for i in range(2, len(S) + 1):
    this_s = S[start_point:i]
    if not (prev_s == S[start_point:i]):
        prev_s = S[start_point:i]
        start_point = i
        count += 1


print(count)

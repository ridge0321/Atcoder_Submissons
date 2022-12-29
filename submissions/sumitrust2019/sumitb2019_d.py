N = int(input())
S = list(str(input()))
int_S = list(map(int, S))
num_count = {}

for i in range(10):
    num_count[i] = []

for i in range(len(int_S)):
    num_count[int_S[i]].append(i)

# print(num_count)
num_temprate = []

for i in range(10):
    for j in range(10):
        for k in range(10):
            num_temprate.append([i, j, k])

count = 0
for l in num_temprate:
    pin1 = l[0]
    pin2 = l[1]
    pin3 = l[2]

    if not (len(num_count[pin1]) == 0 or len(num_count[pin2]) == 0 or len(num_count[pin3]) == 0):
        prev_index = num_count[pin1][0]

        for i in range(len(num_count[pin2])):
            if num_count[pin2][i] > prev_index:
                prev_index = num_count[pin2][i]
                break
        else:
            continue

        for i in range(len(num_count[pin3])):
            if num_count[pin3][i] > prev_index:
                prev_index = num_count[pin3][i]
                count += 1
                break


print(count)

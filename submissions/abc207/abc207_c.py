N = int(input())

closed_interval_list = []
for i in range(N):
    t, l, r = map(int, input().split())

    if t == 2:
        r = r - 0.1

    elif t == 3:
        l = l + 0.1

    elif t == 4:
        r = r - 0.1
        l = l + 0.1

    closed_interval_list.append([t, l, r])

count = 0
for i in range(N - 1):
    l_host = closed_interval_list[i][1]
    r_host = closed_interval_list[i][2]

    for j in range(i + 1, N):
        l_guest = closed_interval_list[j][1]
        r_guest = closed_interval_list[j][2]

        if l_host <= l_guest:
            if r_host >= l_guest:
                count += 1
        else:
            if l_host <= r_guest:
                count += 1

print(count)

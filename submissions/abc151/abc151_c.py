N, M = map(int, input().split())
pS = [list(input().split()) for i in range(M)]

submit_log = {}

if M == 0:
    print("0 0")
    quit()

for ps in pS:
    pi = ps[0]
    si = ps[1]

    if pi not in submit_log:
        if si == "AC":
            submit_log[pi] = [si, 0]
        else:
            submit_log[pi] = [si, 1]
    else:
        if not (submit_log[pi][0] == "AC"):
            if si == "AC":
                submit_log[pi][0] = "AC"
            else:
                submit_log[pi][1] += 1

# print(submit_log)

penalty_count = 0
ac_count = 0
for v in submit_log.values():
    if v[0] == "AC":
        penalty_count += v[1]
        ac_count += 1

print("%d %d" % (ac_count, penalty_count))

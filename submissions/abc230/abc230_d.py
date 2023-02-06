N, D = map(int, input().split())
section = [list(map(int, input().split())) for i in range(N)]

section.sort(key=lambda x: x[1])

ans = 1

punch_sec_left = section[0][1]
punch_sec_right = section[0][1] + D - 1

for sec in section:
    is_in_sec = max(punch_sec_left, sec[0]) <= min(punch_sec_right, sec[1])
    if not is_in_sec:
        ans += 1
        punch_sec_left = sec[0]
        punch_sec_right = sec[1] + D - 1


print(ans)

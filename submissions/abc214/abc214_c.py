N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

first_time_l = []

for t in T:
    first_time_l.append(t)

for i in range(1, N):
    first_time_l[i] = min(first_time_l[i], first_time_l[i - 1] + S[i - 1])

first_time_l[0] = min(first_time_l[0], first_time_l[-1] + S[-1])

for i in range(1, N):
    first_time_l[i] = min(first_time_l[i], first_time_l[i - 1] + S[i - 1])


for t in first_time_l:
    print(t)
N = int(input())
S = [str(input()) for i in range(N)]

s_dict = {}

for i in range(N):
    s = S[i]
    if s not in s_dict:
        s_dict[s] = 1
        print(i + 1)

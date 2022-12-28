N = int(input())
S = list(str(input()))
# print(S)
# check = []
b_flag = False

for i in range(N):
    if b_flag:
        if S[i] == '"':
            b_flag = False

    else:
        if S[i] == '"':
            b_flag = True
        elif S[i] == ",":
            S[i] = "."

# for i in range(N):
#     print(S[i], end="")

print("".join(S))

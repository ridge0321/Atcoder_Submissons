S = list(str(input()))
T = list(str(input()))

for i in range(len(S)):
    s = S[i : len(S)]
    s[len(s) : len(s)] = S[0:i]

    if s == T:
        print("Yes")
        break
else:
    print("No")

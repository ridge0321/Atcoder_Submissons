S = list(str(input()))

ans = [0, 0, 0]

if S[0] == "A":
    ans[0] = 1

terms_2_list = S[2 : len(S) - 1]
if terms_2_list.count("C") == 1:
    ans[1] = 1

    for i in range(len(S)):
        if not (i == 0 or i == terms_2_list.index("C") + 2):
            if S[i] < "a" or "z" < S[i]:
                break

    else:
        ans[2] = 1

if sum(ans) == 3:
    print("AC")
else:
    print("WA")

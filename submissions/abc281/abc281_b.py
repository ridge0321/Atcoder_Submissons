S = list(str(input()))
ans = "Yes"

if not (len(S) == 8):
    print("No")
    quit()


if not ("A" <= S[0] and S[0] <= "Z"):
    ans = "No"


if not ("A" <= S[7] and S[7] <= "Z"):
    ans = "No"

for i in range(1, 7):
    if i == 1:
        if not ("1" <= S[i] and S[i] <= "9"):
            ans = "No"
    else:
        if not ("0" <= S[i] and S[i] <= "9"):
            ans = "No"

print(ans)

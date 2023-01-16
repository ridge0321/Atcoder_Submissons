S = list(str(input()))
T = list(str(input()))
ans = ""
if len(S) < len(T):
    ans = "No"
else:
    for i in range(0, len(S) - len(T) + 1):
        if S[i : i + len(T)] == T:
            ans = "Yes"
            break
    else:
        ans = "No"

print(ans)

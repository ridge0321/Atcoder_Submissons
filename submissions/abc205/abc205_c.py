A, B, C = map(int, input().split())

if C % 2 == 0:
    if abs(A) > abs(B):
        ans = ">"
    elif abs(A) < abs(B):
        ans = "<"
    else:
        ans = "="
else:
    if (A >= 0 and B >= 0) or (A < 0 and B < 0):
        if abs(A) > abs(B):
            ans = ">"
        elif abs(A) < abs(B):
            ans = "<"
        else:
            ans = "="
    elif A < 0:
        ans = "<"
    else:
        ans = ">"

if A == B:
    ans = "="


print(ans)

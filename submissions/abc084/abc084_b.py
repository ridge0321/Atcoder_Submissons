A, B = map(int, input().split())
S = list(str(input()))

s_a = S[0:A]
hyphen = S[A]
s_b = S[A + 1 : len(S)]

# print(s_a, hyphen, s_b)
ans = "Yes"

for a in s_a:
    if a == "-":
        ans = "No"

if not (hyphen == "-") or not (len(s_b) == B):
    ans = "No"

for b in s_b:
    if b == "-":
        ans = "No"

print(ans)

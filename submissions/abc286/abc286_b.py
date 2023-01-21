N = int(input())
S = list(str(input()))
prev = S[0]
result = [prev]

for i in range(1, len(S)):
    if prev == "n":
        if S[i] == "a":
            result.append("y")
            result.append("a")
            prev = "a"
        else:
            result.append(S[i])
            prev = S[i]
    else:
        result.append(S[i])
        prev = S[i]

print("".join(result))

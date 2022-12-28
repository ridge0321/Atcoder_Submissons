S = list(str(input()))

differ_abs = []
for i in range(len(S) - 2):

    num = int("".join(S[i : i + 3]))
    differ_abs.append(abs(753 - num))

print(min(differ_abs))

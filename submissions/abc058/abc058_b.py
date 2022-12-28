O = list(str(input()))
E = list(str(input()))

len_OE = len(O) + len(E)

for i in range(len(E)):
    print(O[i], end="")
    print(E[i], end="")
else:
    if len(O) > len(E):
        print(O[len(O) - 1], end="")

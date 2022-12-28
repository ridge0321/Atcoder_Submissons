N = int(input())

ij_list = []

for i in range(1, int(N ** (1 / 2) + 1)):
    j = N // i
    if i * j == N:
        ij_list.append(i + j)
print(min(ij_list) - 2)

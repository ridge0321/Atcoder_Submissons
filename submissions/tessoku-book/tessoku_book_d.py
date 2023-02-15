N = int(input())

bit_n = bin(N)[2:]

front_0_num = 10 - len(str(bit_n))

for i in range(front_0_num):
    print(0, end="")
print(bit_n)

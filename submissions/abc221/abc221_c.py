from collections import deque

N = list(str(input()))
n_int_list = list(map(int, N))

# for bitnum in range(1,(1 << len(N)) - 1):

max_result = 0
for bitnum in range(1, 2 ** len(N) - 1):

    bitnum_list = list(str(bin(bitnum)))[2:]
    # print(bitnum_list)
    # print(len(N) - len(bitnum_list))
    bitnum_deque = deque(bitnum_list)
    for i in range(len(N) - len(bitnum_list)):
        bitnum_deque.appendleft("0")
    # print(list(bitnum_deque))

    A = []
    B = []

    for i in range(len(N)):
        if bitnum_deque[i] == "0":
            A.append(N[i])
        else:
            B.append(N[i])

    A.sort(reverse=True)
    B.sort(reverse=True)

    A = int("".join(A))
    B = int("".join(B))

    max_result = max(A * B, max_result)

print(max_result)

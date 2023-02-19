T = int(input())
for _ in range(T):
    N = int(input())
    s = str(input())
    S = list(s)
    # bit_s = int(str(input()), 2)

    # print(bit_s)
    one_count = S.count("1")
    # one_count = bin(bit_s).count("1")

    if one_count % 2 == 1:
        print(-1)

    elif N == 3:
        if s == "011" or s == "110":
            print(-1)
        elif s == "000":
            print(0)
        else:
            print(1)

    elif N == 4:
        if s == "0110":
            print(3)
        elif s == "0011" or s == "1100":
            print(2)
        else:
            print(one_count // 2)

    elif one_count == 2:
        if "11" in s:
            print(2)
        else:
            print(1)

    else:
        print(one_count // 2)

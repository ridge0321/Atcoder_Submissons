N = int(input())
S = [list(str(input())) for i in range(N)]

query1 = ["H", "D", "C", "S"]
query2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
stack = []

for s in S:
    if s[0] not in query1:
        print("No")
        quit()

    elif s[1] not in query2:
        print("No")
        quit()

    elif s in stack:
        print("No")
        quit()

    else:
        stack.append(s)
else:
    print("Yes")

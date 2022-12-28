S = list(str(input()))


stack = [[]]
box = []


for i in range(len(S)):
    if S[i] == "(":
        stack.append([])

    elif "a" <= S[i] and S[i] <= "z":
        if S[i] in box:
            print("No")
            quit()
        else:
            stack_top = stack.pop()
            stack_top.append(S[i])
            stack.append(stack_top)
            box.append(S[i])

    elif S[i] == ")":
        temp_box = []
        stack_top = stack.pop()
        for b in box:
            if b not in stack_top:
                temp_box.append(b)
        box = temp_box

else:
    print("Yes")

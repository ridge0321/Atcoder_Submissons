N = int(input())
st_dict = {}
s_list = []

for i in range(N):
    s, t = map(str, input().split())
    st_dict[s] = [t, False]
    s_list.append(s)

for s in s_list:
    count = 0
    if st_dict[s][1] == True:
        continue
    prev_s = s
    while count < N * 2 + 10:
        if st_dict.get(prev_s, "None") == "None":
            break

        elif st_dict[prev_s][1] == True:
            prev_s = st_dict[prev_s][0]
            count += 1

        elif st_dict[prev_s][1] == False:
            st_dict[prev_s][1] = True
            prev_s = st_dict[prev_s][0]
            count += 1

    else:
        # print(count)
        print("No")
        quit()


print("Yes")

N = int(input())
a, b, c = map(int, input().split())

l_coin = max(a, b, c)
s_coin = min(a, b, c)
m_coin = (a + b + c) - (l_coin + s_coin)

l_max = min(N // l_coin + 1, 10000)
ans_l = []
temp_l = []

for l_num in reversed(range(l_max)):
    remain_l = N - l_coin * l_num
    m_max = min(remain_l // m_coin + 1, 10000 - l_num)
    temp_l.append(m_max)

    for m_num in reversed(range(m_max)):
        remain_m = remain_l - m_coin * m_num
        s_max = min(remain_m // m_coin + 1, 10000 - (l_num + m_num))

        if remain_m % s_coin == 0:
            s_num = remain_m // s_coin

            ans_l.append(l_num + m_num + s_num)

            # print(l_num)
            # print(m_num)
            # print(s_num)
            # print(l_num * l_coin + m_num * m_coin + s_num * s_coin)
            # print(l_num + m_num + s_num)
            # quit()

# print(max(temp_l))
print(min(ans_l))
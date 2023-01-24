def is_in_24_hour(h, m):
    if 0 <= h and h < 24 and 0 <= m and m < 60:
        return True
    else:
        return False


H, M = map(int, input().split())


h_copy = H
m_copy = M

while True:
    h2 = h_copy // 10
    h1 = h_copy % 10
    m2 = m_copy // 10
    m1 = m_copy % 10

    h2_swap = h2 * 10 + m2
    h1_swap = h1 * 10 + m1

    if is_in_24_hour(h2_swap, h1_swap):

        print(h_copy, m_copy)
        quit()

    else:
        m_copy += 1

        if m_copy > 59:
            m_copy = 0
            h_copy += 1
            if h_copy > 23:
                h_copy = 0

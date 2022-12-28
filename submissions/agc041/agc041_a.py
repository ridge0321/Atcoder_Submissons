N, A, B = map(int, input().split())

if (B - A) % 2 == 1:
    # # 端の宅につくまでの手数
    # # B
    # N - B +1
    # # そのときのA
    # A + N - B+1
    # A + N - B
    # # そこから合流までの手数
    # if (A + N - B) == N - 1:
    #     edge_large = 1 + N - B
    # else:
    #     edge_large = N - 1 - (A + N - B)

    edge_large = (N - B + 1) + (N - (A + N - B + 1)) // 2

    # # A
    # A - 1
    # # そのときのB
    # B - (A - 1)
    # if (B - (A - 1)) == 2:
    #     edge_small = 1 + A - 1
    # else:
    #     edge_small = B - (A - 1) - 1

    edge_small = A + (B - A - 1) // 2

    print(min(edge_large, edge_small))

else:
    print((B - A) // 2)

Q = int(input())
TX = [list(map(int, input().split())) for i in range(Q)]

deck = []
for i in range(Q):
    tx = TX[i]
    ti = tx[0]
    xi = tx[1]

    if ti == 1:
        deck.insert(0, xi)
    elif ti == 2:
        deck.append(xi)
    else:
        print(deck[xi - 1])

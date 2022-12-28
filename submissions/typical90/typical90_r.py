import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for i in range(Q)]


for ei in E:
    theta = math.radians((360 * ei) / T)
    ex = 0
    ey = -(L / 2) * math.sin(theta)
    ez = (L / 2) - (L / 2) * math.cos(theta)

    e_to_c_dis_xy = (X**2 + (Y - ey) ** 2) ** 0.5

    radian = math.atan2(ez, e_to_c_dis_xy)
    print(math.degrees(radian))

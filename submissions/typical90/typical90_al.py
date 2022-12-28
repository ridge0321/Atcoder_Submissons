import math

A, B = map(int, input().split())


def lcm_r(a, b):
    remainder = a % b
    if remainder == 0:
        return a
    return a * lcm_r(b, remainder) // remainder


lcm = lcm_r(A, B)
if lcm > 10**18:
    ans = "Large"
else:
    ans = lcm
print(ans)

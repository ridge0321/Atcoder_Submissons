import functools
import math

abc = list(map(int, input().split()))
# print(abc)
# reduce()でリスト内の最大公約数を求める
gcd = functools.reduce(math.gcd, abc)
# print(gcd)
result = []
for r in abc:
    result.append(r // gcd - 1)
# print(result)
print(int(sum(result)))

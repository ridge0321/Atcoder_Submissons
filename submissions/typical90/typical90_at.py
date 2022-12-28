N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
amod_count = {}
bmod_count = {}
cmod_count = {}
for i in range(46):
    amod_count[i] = 0
    bmod_count[i] = 0
    cmod_count[i] = 0

for i in range(N):
    amod_count[A[i] % 46] += 1
    bmod_count[B[i] % 46] += 1
    cmod_count[C[i] % 46] += 1

for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += amod_count[i] * bmod_count[j] * cmod_count[k]

print(ans)

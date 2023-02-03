def Eratosthenes(num):
    is_prime_list = [True] * (num + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False
    i = 2
    while i**2 <= num:
        if is_prime_list[i] == False:
            i += 1
            continue

        j = 2
        while i * j <= num:
            is_prime_list[i * j] = False
            j += 1
        i += 1

    result = []

    for i in range(len(is_prime_list)):
        if is_prime_list[i]:
            result.append(i)

    return result


N = int(input())

prime_list = Eratosthenes(10**6 + 1)

ans = 0
right = len(prime_list) - 1
for left in range(len(prime_list)):

    while left < right and prime_list[left] * (prime_list[right] ** 3) > N:
        right -= 1
    if left > right:
        break

    ans += right - left

print(ans)

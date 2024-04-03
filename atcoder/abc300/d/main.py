n = int(input())
sieve = [1] * (int(n**0.5) + 1)
primes = []

# sieve は √n + 1 個の「素数なら1」のlist, primesは素数のlist
for p in range(2, len(sieve)):
    if sieve[p] == 0:
        continue
    primes.append(p)
    for j in range(p * p, len(sieve), p):
        sieve[j] = 0

# prefix_sum[n] : (n 以下の素数の個数) 
prefix_sum = sieve
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i]

# print(sieve, primes, prefix_sum)
ans = 0

# a, b を全探索する
for i in range(len(primes)):
    a = primes[i]
    if a * a * a * a >= n:
        break
    for j in range(i + 1, len(primes)):
        b = primes[j]
        if a * a * b * b * b >=n:
            break
        ans += prefix_sum[int((n // (a * a * b))**0.5)] - prefix_sum[b]

print(ans)
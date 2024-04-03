# 愚直loop、ロジックは正しいがタイムアウトになる
n = int(input())
print(n)

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

count = 0
for a in range(2, n+1):
    if is_prime(a):
        for b in range(a+1, n+1):
            if is_prime(b):
                for c in range(b+1, n+1):
                    if is_prime(c) and a**2 * b * c**2 <= n:
                        count += 1
print(count)

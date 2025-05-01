from math import sqrt
n = int(input())

# i * j = n
# ans = (i-1) + (j-1)
j = 1
for i in range(2, int(sqrt(n)) + 2):
    if n % i == 0:
        j = i
print(min((j - 1) + (n // j - 1), n - 1))

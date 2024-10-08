def is_prime(x: int) -> bool:
    if x <= 1: 
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

x = int(input())
a = x
while is_prime(a) == False:
    a += 1

print(a)

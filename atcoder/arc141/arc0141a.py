#!/usr/local/python
import sys
import math
def I(): return int(sys.stdin.readline().rstrip())


def isPrime(num):
  if num == 2:
    return True
  if num % 2 == 0:
    return False
  
  # nの平方根まで計算する
  m = math.floor(math.sqrt(num)) + 1
  for p in range(3, m, 2):
      if num % p == 0:
        return False
  return True


def divisor_list_s(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)  
            if i**2 == num:
                continue
            divisors.append(int(num/i))
    
    return sorted(divisors, reverse=True) # 降順


t = I()
for _ in range(t):
  str_n = (sys.stdin.readline().rstrip())
  int_n = int(str_n)

  if isPrime(len(str_n)) and len(str_n) >= 4:
    if int(str_n[0] * len(str_n)) > int_n:
      a_str = str(int(str_n[0])-1)
    else:
      a_str = str_n[0]
    ans = a_str * len(str_n)
    print("isprime:", ans)
  
  else:
    n_div_list = divisor_list_s(len(str_n)) # 約数list

    a = n_div_list[1] # 自分以外の最大約数
    b = n_div_list[-2] # 1以外の最小約数

    if int(str_n[:a] * b) > int_n:
      a -= 1

    ans = str_n[:a] * b
    print(ans)

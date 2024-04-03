# ビット全探索（2^n 通りの全探索）
N = sorted(input(),reverse=True)
ans = 0
for i in range(1<<len(N)):
  l = 0
  r = 0
  for j in range(len(N)):
    print("i, j, i & (1<<j):", i, j, i & (1<<j))
    if i & (1<<j):
      l = l*10+ord(N[j])-ord('0')
      print("1<<j, l: ", 1<<j, l)
    else:
      r = r*10+ord(N[j])-ord('0')
      print("1<<j, r: ", 1<<j, r)
  print("ans, l*r: ", ans, l*r)
  ans = max(ans, l*r)
print(ans)

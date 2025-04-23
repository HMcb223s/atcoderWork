n = int(input())
a = list(map(int, input().split()))

# 数列 A に似ている数列 b は 3**n 個
# すべての i について bi が奇数となるような数列 b の個数 を求める
# Ai が偶数のとき、bi = Ai − 1 または bi = Ai + 1
# Ai が奇数のとき、bi = Ai 
# Ai が偶数である i の個数を e とすると、このような数列 b は 2**e 個
cnt = 0
for i in range(n):
    if a[i] % 2 == 0:
        cnt += 1
print(3**n - 2**cnt)

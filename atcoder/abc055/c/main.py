n, m = map(int, input().split())
# print(m // 2, (2 * n + m) // 4)
print(min(m // 2, (2 * n + m) // 4))

# 別解
# count=0
# if n>=m//2:
#     count+=m//2
#     m=0
# else:
#     count+=n
#     m-= n*2
# count+=m//4
# print(count)
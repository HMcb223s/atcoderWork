n, k = map(int, input().split())

cnt = [0] * (10 ** 5)
for _ in range(n):
    a, b = map(int, input().split())
    cnt[a - 1] += b

i = 0
while k > 0:
    k -= cnt[i]
    i += 1
print(i)

# 別解

# N,K=map(int,input().split())
# A=list(list(map(int,input().split())) for _ in range(N))
# A.sort()
# i=0
# cnt=0
# while K>cnt:
#   cnt+=A[i][1]
#   i+=1
# print(A[i-1][0])

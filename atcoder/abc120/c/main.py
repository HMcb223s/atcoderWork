s = input()
n = len(s)

cnt =[0, 0]
for i in range(n):
    if s[i] == '0':
        cnt[0] += 1
    if s[i] == '1':
        cnt[1] += 1
print(min(cnt[0], cnt[1]) * 2)

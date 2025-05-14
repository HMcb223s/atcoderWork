from collections import Counter


n = int(input())
a = list(map(int, input().split()))

a_count = list(Counter(a).items())
a_count.sort(key=lambda x: x[0], reverse=True)
# print(a_count)

ans = [0, 0]
ans_idx = 0 # 片方は0 もう片方は1
for x, cnt in a_count:
    if cnt >= 4 and ans_idx == 0: # 正方形
        ans = [x, x]
        break
    
    if cnt >= 2:
        ans[ans_idx] = x
        ans_idx += 1
    
    if ans_idx == 2:
        break

print(ans[0] * ans[1])

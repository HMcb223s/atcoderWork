N = int(input())
S = input()

ans = 0
dig = [-1, -1, -1]
for i in range(1000):
    dig = list(map(str, [i//100, (i//10) % 10, i%10]))

    dig_idx = 0
    for j in range(N):
        if dig_idx >= 3:
            break
        if S[j] == dig[dig_idx]:
            dig_idx += 1 
        if dig_idx == 3:
            ans += 1

print(ans)

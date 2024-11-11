def conv(s):
    n = len(s)
    runlength = []
    l, r = 0, 1
    while l < n:
        while r < n and s[l] == s[r]:
            r += 1

        runlength.append((s[l], r - l))
        l = r
        r += 1
    return runlength

s, t  = conv(input()), conv(input())
s_n, t_n = len(s), len(t)

if s_n != t_n:
    print("No")
    exit()

for i in range(t_n):  
    s_chr, s_cnt = s[i]
    t_chr, t_cnt = t[i]
    # print(s_chr, s_cnt, t_chr, t_cnt)
    if s_chr != t_chr or s_cnt > t_cnt:
        print("No")
        exit()
    if s_cnt < t_cnt and s_cnt == 1:
        print("No")
        exit()
    
print("Yes") 


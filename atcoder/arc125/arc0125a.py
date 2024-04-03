N, M = map(int,input().split()) 
S = list(map(int,input().split()))
T = list(map(int,input().split()))

ans = -1

if not 0 in S :
    if not 1 in T :
        print(ans)
elif not 1 in S :
    if not 0 in T :
        print(ans)
else :
    r_count = S.index(T[0])
    l_count = list(reversed(S)).index(T[0])

    if r_count <= l_count :
        ans = r_count
    else :
        ans = l_count + 1

    tmp = -1
    for i in range(M):
        if i == 0:
            ans = ans + 1
            tmp = T[i]
        elif tmp == T[i] :
            ans = ans + 1
        else :
            ans = ans + 2
            tmp = T[i]
    
    print(ans)


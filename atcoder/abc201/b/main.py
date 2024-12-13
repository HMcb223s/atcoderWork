n = int(input())
st = []

for i in range(n):
    s, t =input().split()
    st.append([int(t), s])

print(sorted(st, reverse=True)[1][1])


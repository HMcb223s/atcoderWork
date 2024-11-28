c = [list(map(int, input().split())) for i in range(3)]

row_flg_1 = (c[1][0] - c[0][0] == c[1][1] - c[0][1] == c[1][2] - c[0][2])
row_flg_2 = (c[2][0] - c[1][0] == c[2][1] - c[1][1] == c[2][2] - c[1][2])
col_flg_1 = (c[0][1] - c[0][0] == c[1][1] - c[1][0] == c[2][1] - c[2][0])
col_flg_2 = (c[0][2] - c[0][1] == c[1][2] - c[1][1] == c[2][2] - c[2][1])

if row_flg_1 and row_flg_2 and col_flg_1 and col_flg_2:
    print("Yes")
else:
    print("No")

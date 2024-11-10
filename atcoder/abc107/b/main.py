h, w = map(int, input().split())
a = [input() for i in range(h)]

a_r = [row for row in a if '#' in row]
# for _ in a_r:
    # print(''.join(_))

# 転置
a_r_transposed = list(map(list, zip(*a_r)))
a_rc_transposed = [col for col in a_r_transposed if '#' in col]
ans = list(map(list, zip(*a_rc_transposed)))

for _ in ans:
    print(''.join(_))

# # 失敗 （出力結果が間違っています）

# n, m, k = map(int, input().split())
# # 前提: m < n

# step_map = {}
# shigemi = [-1] * n
# r = [-1] * m
# for i in range(m):
#     r[i] = int(input()) - 1 # 0-indexed
#     shigemi[r[i]] = r[i]

# # print(f'{r=},     {shigemi=}')
# for i in r:
#     tmp_i = shigemi[i]
#     cnt = 0
#     while True:
#         tmp_i = (tmp_i + 1) % n
#         cnt += 1

#         if shigemi[tmp_i] == -1:
#             shigemi[tmp_i], shigemi[i] = shigemi[i], -1
#             step_map[i] = cnt
#             break

#     # print(f'{i=}, {tmp_i=}, {shigemi=}, {step_map=},')

# for map_key, map_value in step_map.items():
#     print((map_key + map_value * k) % n + 1)

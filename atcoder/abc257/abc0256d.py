#!/usr/local/python
import copy
n = int(input())

ans_l = [0]
ans_r = [0]

ans_l[0], ans_r[0] = map(int, input().split())
for _ in range(n-1):
  l, r = map(int, input().split())

  tmp_ans_l = copy.deepcopy(ans_l)
  tmp_ans_r = copy.deepcopy(ans_r)

  for i, (idx_l, idx_r) in enumerate(zip(ans_l, ans_r)):

    print("idx_r, idx_l , r, l : ", idx_r, idx_l , r, l)

    if idx_r >= l and idx_r < r:
      tmp_ans_r[i] = r
    


    print(idx_l, idx_r)
  
  ans_l = copy.deepcopy(tmp_ans_l)
  ans_r = copy.deepcopy(tmp_ans_r)

print(ans_l, ans_r)

#lr = [map(float, input().split()) for _ in range(n)]
#l, r = [list(i) for i in zip(*lr)]


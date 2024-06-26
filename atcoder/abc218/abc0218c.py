#!/usr/local/python

N = int(input())
# グリッドを読み込んで#の位置の集合を返す
def read():
  S = set()
  for y in range(N):
    l = input()
    for x in range(N):
      if l[x]=="#":
        S.add((x, y))
  return S

S = read()
T = read()

print(S)
print(T)


for _ in range(4):
  # 最も左（複数あればそのうちで最も上）の#を(0, 0)の位置にする
  mx, my = min(S)
  S = set((x-mx, y-my) for x, y in S)
  mx, my = min(T)
  T = set((x-mx, y-my) for x, y in T)
  if S == T:
    print("Yes")
    exit(0)
  # Tを回転
  T = set((y, -x) for x, y in T)
print("No")

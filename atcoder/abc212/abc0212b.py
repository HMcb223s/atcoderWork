#!/usr/local/python
# abc212 b 
a = input()
same, step = True, True
for i in range(3):
    if a[i] != a[i+1]:
        same = False
    if (int(a[i])+1)%10 != int(a[i+1]):
        step = False
if(same or step):
    print("Weak")
else:
    print("Strong")
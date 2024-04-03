S = input().strip()
B_indices = [i for i in range(8) if S[i] == 'B']
R_indices = [i for i in range(8) if S[i] == 'R']
K_index = S.index('K')

# Check condition 1
if B_indices[0] % 2 == B_indices[1] % 2:
    print("No")
    exit()

# Check condition 2
if (R_indices[0] > K_index):
    print("No")
    exit()

if (K_index > R_indices[1]):
    print("No")
    exit()

print("Yes")

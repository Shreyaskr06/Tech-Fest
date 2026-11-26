n, m = map(int, input().split())
A = []
total = 0

for i in range(n):
    B = list(map(int, input().split()))
    A.append(B)
for ele in B:
    if ele == 0:
        total += [[ele]]
    if ele == -1:
        total += [[ele]]
print(total)

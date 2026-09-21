import math
D : list[str]= input().split()
maximum : float = -201.
num : int = 0

for i in range(len(D) - 1):
    m : float = math.fabs(int(D[i]) - int(D[i + 1]))
    if m > maximum:
        maximum = m
        num = i

print(num, num + 1)
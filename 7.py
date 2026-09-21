import math
D : list[str]= input().split()
maximum : int = -201
num : int = 0

for i in range(len(D) - 1):
    if int(D[i]) > int(D[i + 1]):
        if  math.fabs(int(D[i]) - int(D[i + 1])) > maximum:
            maximum = int(D[i])
            num = i

    else:
        if math.fabs(int(D[i + 1]) - int(D[i])) > maximum:
            maximum = int(D[i])
            num = i
print(num, num + 1)

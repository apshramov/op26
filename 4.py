D : list[str] = input().split()
mini : int = 101
num : int = 0
maxi : int = -101

for i in range(len(D)):
    if int(D[i]) < mini:
        mini = int(D[i])
        num = int(D[i])

for i in range(num, len(D)):
    if int(D[i]) > maxi:
        maxi = int(D[i])

print(mini, maxi)
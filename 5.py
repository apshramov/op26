D : list[str]= input().split()
maxi : int = -201
num : int = 0

for i in range(len(D) - 1):
    if int(D[i]) + int(D[i + 1]) > maxi:
        maxi = int(D[i])
        num = i

print(num, num + 1)
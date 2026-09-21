D : list[str]= input().split()
maxi : int = -301
num : int = 0

for i in range(len(D) - 2):
    m : int = int(D[i]) + int(D[i + 1]) + int(D[i + 2])
    if m > maxi:
        maxi = m
        num = i

print(num, num + 1, num + 2)
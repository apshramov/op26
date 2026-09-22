N : int = int(input())
max : int = 0
last_2 : int = 0
last : int = 0
for i in range(N):
    N_2 : int = int(input())
    if i == 0:
        last_2 = N_2
    elif i == 1:
        last = N_2
    else:
        if last_2 < last > N_2:
            max += 1
print(max)
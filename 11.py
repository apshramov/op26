N = int(input())
count = 0
count_2 = 0
cif = 0
for i in range(N):
    N_2 = int(input())
    if i == 0:
        cif = N_2
    else:
        if N_2 == cif:
            count_2 += 1
        else:
            if count_2 > 1:
                if count_2 > count:
                    count = count_2
                    count_2 = 0
print(count)
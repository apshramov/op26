a = input().split()
count = 0
count_2 = 0
for i in range(3, len(a)):
    if a[i] == a[i-2]:
        count_2 += 2
        if count_2 > count:
                count = count_2
print(count)

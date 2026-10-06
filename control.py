N = int(input())
max = 0
last = 0
for i in range(N):
    n = int(input())
    if i == 0:
        last = n
    else:
        if n + last > max:
            max = last + n
        last = n
print(max)
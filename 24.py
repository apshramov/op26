counter = 0
N = int(input())
a = int(input())
b = int(input())
for i in range(N - 2):
    c = int(input())
    if c < b > a or a > b < c:
        counter += 1
    a = b
    b = c
print(counter)
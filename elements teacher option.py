counter = 2
max_counter = 2
N = int(input())
a = int(input())
b = int(input())

for i in range(N - 2):
    c = int(input())
    if c == a:
        counter += 1
    else:
        counter = 2
    max_counter = max(max_counter, counter)
    a = b
    b = c
print(max_counter)

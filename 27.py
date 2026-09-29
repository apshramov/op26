counter = 0
counter_2 = 0
max_counter = 0
N = int(input())
a = int(input())
b = int(input())
for i in range(N - 2):
    c = int(input())
    if c < b < a:
        counter += 1
    elif c > b and b < a:
        pass
    elif a < b and b < c:
        counter_2 += 1
    elif a < b > c:
        pass
    else:
        counter_2 = 0
        count = 0
    max_counter = max(counter + counter_2, max_counter)
    a = b
    b = c
print(max_counter + 1)
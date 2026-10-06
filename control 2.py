N = int(input())
number = 0
max = 0
last = 0
for i in range(N):
	n = int(input())
	if i == 0:
		last = n
	else:
		if n + last > max:
			max = n + last
			number = i
		last = n
print(number, number + 1)
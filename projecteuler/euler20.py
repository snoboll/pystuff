from math import factorial

sum = 0
for c in str(factorial(100)):
	sum = sum + int(c)

print(sum)
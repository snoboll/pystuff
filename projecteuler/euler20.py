class factorial(n):
	if n == 1:
		return 1
	else:
		return factorial(n-1)*n

fact = factorial(100)
sum = 0
for c in str(fact):
	sum = sum + int(c)
print(sum)

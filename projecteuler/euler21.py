#Euler21
divsumdict = {}

def divs(i):
	divisors = []
	for n in range(1, i):
		if i%n == 0:
			divisors.append(n)
	return divisors
	
for i in range(1,10000):
	addsum = sum(divs(i))
	#print(addsum)
	divsumdict[i] = addsum

ans = 0
for i in range (1, len(divsumdict)):
	for j in range(1, len(divsumdict)):
		if (divsumdict[j] == i) and (divsumdict[i] == j) and i!=j:
			print("adding",i)
			ans+=i
	
print("done")
print(ans)
#print(divsumdict)
	

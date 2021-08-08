with open('euler13input.txt', 'r') as f:
	f_contents = f.readlines()
	
	sum = 0
	for s in f_contents:
		sum = sum + int(s)

print(sum)	
f.close()
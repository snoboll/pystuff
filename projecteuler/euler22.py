#Euler22
inputfile = open("p022_names.txt","r")
a = inputfile.readline().split(",")

a.sort()
nameval = 0

ans = 0
for n in range(len(a)):
	name = a[n]
	print(name)
	nameval = 0
	for i in range(1,len(name)-1):
		add = ord(name[i]) - 64
		print("adding", add)
		nameval += add

	print(nameval, "with factor:", n+1)
	print("total name value", nameval*(n+1))
	ans += nameval*(n+1)
	print("current ans", ans)

print(ans)

#euler 18
f = open("euler18input.txt", "r")

tree = [[0] for i in range(15)]

for i in range(13,-1,-1):
	print(i)

for i in range(15):
	f1 = f.readline().split()
	f2 = [int(i) for i in f1]
	tree[i] = f2

ans = 0
for i in range(13,-1,-1):
	for j in range(i+1):
		tree[i][j] += max(tree[i+1][j], tree[i+1][j+1])

print(tree)
print(tree[0][0])

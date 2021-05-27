#euler 67
f = open("euler67input.txt", "r")

def row_count(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i+1

rows = row_count("euler67input.txt")

tree = [[0] for i in range(rows)]

for i in range(rows):
	f1 = f.readline().split()
	f2 = [int(i) for i in f1]
	tree[i] = f2

for i in range(rows-2,-1,-1):
	for j in range(i+1):
		tree[i][j] += max(tree[i+1][j], tree[i+1][j+1])

print(tree)
print(tree[0][0])

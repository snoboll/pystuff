l = []

for a in range(2, 101):
    for b in range(2, 101):
        if (a ** b not in l):
            l.append(a ** b)
        if (b ** a not in l):
            l.append(b ** a)

l.sort()
print(len(l))
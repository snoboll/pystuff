#euler29
mylist = []
for a in range(2, 101):
    for b in range(2, 101):
        if (a**b not in mylist):
            mylist.append(a**b)
        if (b**a not in mylist):
            mylist.append(b**a)
mylist.sort()
print(len(mylist))

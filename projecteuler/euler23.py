#Euler23
import time
start_time = time.time()

#checking abundant numbers
def isAbund(n):
    divs = set()
    divsum = sum([div  for div in range(1,n) if n%div == 0])
    return(divsum>n)

#binary search
def binsearch(list, item):
    hi = len(list)-1
    lo = 0
    found = False
    while lo<=hi and not found:
        mid = (hi+lo)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                hi = mid-1
            else:
                lo = mid+1
    return found

cap = 100

#getting list of abundant numbers
abund = []
for i in range(cap):
    if isAbund(i):
        abund.append(i)
print("abund =", abund)
#getting nums which cant be sum of abund numbers
anslist = []
for n in range(1, cap):
    combofound = False
    for a in abund:#a is first abund number
        b = n-a
        if binsearch(abund, b):
            print(a, "+", b, "=", n)
            combofound = True
            break

    if not combofound:
        anslist.append(n)

print(anslist)
print(sum(anslist))
print("--- %s seconds ---" % (time.time()-start_time))

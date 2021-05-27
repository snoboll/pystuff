# Euler 12

list = [1,3]
first = True

for i in range (3,10000):
    list.append( i + list[i-2])
    element = list[i-1]

    j = 1
    divs = 0
    while j<(element/2):
        if element%j == 0:
            divs = divs +1
        if divs == 100-1 and first:
            svar = element
            first = False
        j = j+1
        
print svar
print 'slut'

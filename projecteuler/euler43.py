import itertools
from tabnanny import check


divlist = [2, 3, 5, 7, 11, 13, 17]
startnum = 1234567890

def checknum(numstring):
    startindex = 1
    endindex = 4

    num = int(numstring[startindex:endindex])
    for divnum in divlist:
        # print("dividing {} with {}".format(num, divnum))
        if num % divnum != 0:
            return False
        
        startindex += 1
        endindex += 1
        num = int(numstring[startindex:endindex])

    return True

def generate_permuts(num):
    numlist = [int(x) for x in str(num)]

    permuts = list(itertools.permutations(numlist))

    ret = []
    for p in permuts:
        if p[0] == "0":
            p = p[1:]
        s = ""
        for i in p:
            s += str(i)
        ret.append(int(s))

    return ret

ans = 0
pms = generate_permuts(1234567890)
for n in pms:
    if checknum(str(n)):
        ans += n
    
print(ans)

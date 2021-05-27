ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens = {0:'', 1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
teens = {0:'', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen', 6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}

sum = 0
for i in range(1,1000):
    stri = str(i)
    numstr = ''

    for index, j in enumerate(stri[::-1]):#looping over reverse string
        intj = int(j)
        if index == 0:#ones
            if len(stri) > 1 and stri[-2] == '1':
                numstr = teens[intj] + numstr
            else:
                numstr = ones[intj] + numstr
        elif index == 1:#tens
            if stri[-2] != '1':
                numstr = tens[intj] + numstr
            elif stri[-2:] == '10':
                numstr += 'ten'
        elif index == 2:#hundreds
            numstr = ones[intj] + 'hundred' + 'and' + numstr
            if stri[-2:] == '00':
                numstr = numstr[:-3]

    print(numstr)
    sum += len(numstr)

print('onethousand')
sum += len('onethousand')

print(sum)

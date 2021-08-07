
def is_palindrome(s):
    if s[0] == '0' or s[-1] == '0':
        return False

    i = 0
    ii = len(s)-1
    while s[i] == s[ii]:
        i += 1
        ii -= 1
        
        if i >= len(s) / 2:
            return True

    return False


if __name__ == '__main__':
    sum = 0
    for i in range(1000000):
        bin_str = str(bin(i))[2:]
        dec_str = str(i)
        if is_palindrome(bin_str) and is_palindrome(dec_str):
            sum += i
    
    print(sum)
    


from helpers import is_palindrome

if __name__ == '__main__':
    sum = 0
    for i in range(1000000):
        bin_str = str(bin(i))[2:]
        dec_str = str(i)
        if is_palindrome(bin_str) and is_palindrome(dec_str):
            sum += i
    
    print(sum)
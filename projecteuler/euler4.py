from helpers import is_palindrome

ans = 0
for i in range(1000, 0, -1):
    for j in range(1000, 0, -1):
        if is_palindrome(str(i*j)):
            if i * j > ans:
                ans = i * j

print(ans)
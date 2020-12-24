word = input().strip()

if word == word[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')

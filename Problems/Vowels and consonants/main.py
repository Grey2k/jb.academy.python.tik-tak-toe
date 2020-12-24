chars = input().strip()

vowel = 'aeiou'

for char in chars:
    if not char.isalpha():
        break

    if char in vowel:
        print('vowel')
        continue

    print('consonant')

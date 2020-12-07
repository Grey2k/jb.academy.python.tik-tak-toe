number = input().strip()

dictionary = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

for char in number:
    print(dictionary[int(char)])

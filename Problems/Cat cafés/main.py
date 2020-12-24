maximum = 0
name = ''

while True:
    data = input().strip()

    if data == 'MEOW':
        break

    cafe, cats = data.split()

    if int(cats) > maximum:
        maximum = int(cats)
        name = cafe

print(name)

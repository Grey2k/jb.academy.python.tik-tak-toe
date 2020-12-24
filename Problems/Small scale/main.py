minimum = None

while True:
    number = input().strip()

    if number == '.':
        break

    if minimum is None or float(number) < minimum:
        minimum = float(number)

print(minimum)

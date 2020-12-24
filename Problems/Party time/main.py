guests = []

while True:
    guest = input().strip()

    if guest == '.':
        break

    guests.append(guest)

print(guests)
print(len(guests))

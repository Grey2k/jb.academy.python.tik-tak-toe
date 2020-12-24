numbers = []

while True:
    char = input().strip()

    if char == '.':
        break

    numbers.append(int(char))

print(sum(numbers) / len(numbers))

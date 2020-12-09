numbers = [int(n) for n in list(input().strip())]

print([sum([n, numbers[i - 1]]) / 2 for i, n in enumerate(numbers) if i > 0])

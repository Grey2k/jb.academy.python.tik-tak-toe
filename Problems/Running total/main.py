numbers = [int(n) for n in list(input().strip())]

sum_list = [n + sum(y for j, y in enumerate(numbers) if j < i) if i > 0 else n for i, n in enumerate(numbers)]

print(sum_list)

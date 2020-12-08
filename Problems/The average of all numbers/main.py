# put your python code here
a = int(input().strip())
b = int(input().strip())

numbers = []
total = 0

for n in range(a, b + 1):
    if n % 3 == 0:
        numbers.append(n)
        total += n

print(total / len(numbers))

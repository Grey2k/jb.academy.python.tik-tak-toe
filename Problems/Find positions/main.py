# put your python code here
numbers = input().split()
needle = input().strip()

result = []

for i, _ in enumerate(numbers):
    if numbers[i] == needle:
        result.append(str(i))

if len(result) > 0:
    print(" ".join(result))
else:
    print('not found')

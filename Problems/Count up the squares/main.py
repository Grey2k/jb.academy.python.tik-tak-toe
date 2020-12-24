# put your python code here

squares = 0
total = 0

first = int(input().strip())

total += first
squares += first ** 2

while total != 0:
    value = int(input().strip())

    total += value
    squares += value ** 2

print(squares)

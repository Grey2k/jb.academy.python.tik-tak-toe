# put your python code here
while True:
    number = int(input().strip())

    if number < 10:
        continue

    if number > 100:
        break

    print(number)

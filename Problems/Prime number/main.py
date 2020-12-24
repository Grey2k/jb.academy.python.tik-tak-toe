number = int(input().strip())

for i in range(number):
    if number <= 1 or (i > 1 and number % i == 0):
        print('This number is not prime')
        break
else:
    print('This number is prime')

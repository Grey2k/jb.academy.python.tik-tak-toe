income = int(input())

if 0 < income <= 15_527:
    tax = 0
elif 15_527 < income <= 42_707:
    tax = 15
elif 42_707 < income <= 132_406:
    tax = 25
else:
    tax = 28

print('The tax for {income} is {percent}%. That is {calculated_tax} dollars!'.format(
    income=income, percent=tax, calculated_tax=round(income * tax / 100)
))

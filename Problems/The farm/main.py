amount = int(input().strip())


def plural_print(count: int, noun: str) -> None:
    plural = noun
    if count > 1 and noun not in ['sheep']:
        plural += 's'

    print(count, plural)


chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if amount < chicken:
    print('None')
elif chicken <= amount < goat:
    plural_print(amount // chicken, 'chicken')
elif goat <= amount < pig:
    plural_print(amount // goat, 'goat')
elif pig <= amount < cow:
    plural_print(amount // pig, 'pig')
elif cow <= amount < sheep:
    plural_print(amount // cow, 'cow')
else:
    plural_print(amount // sheep, 'sheep')

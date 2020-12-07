order = input().strip()

pizza = [
    'Margherita',
    'Four Seasons',
    'Neapolitan',
    'Vegetarian',
    'Spicy'
]

salad = [
    'Caesar salad',
    'Green salad',
    'Tuna salad',
    'Fruit salad'
]

soup = [
    'Chicken soup',
    'Ramen',
    'Tomato soup',
    'Mushroom cream soup'
]

if order == 'pizza':
    print(', '.join(pizza))
elif order == 'salad':
    print(', '.join(salad))
elif order == 'soup':
    print(', '.join(soup))
else:
    print("Sorry, we don't have it in the menu")

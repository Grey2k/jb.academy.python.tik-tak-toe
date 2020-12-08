camel_cased: str = input().strip()

underscored = []

for char in camel_cased:
    if len(underscored) > 0 and char.isupper():
        underscored.append('_')

    underscored.append(char.lower())

print("".join(underscored))

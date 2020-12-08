# write your code here

X = 'X'
Z = 'O'
_ = '_'


def print_field(field: list) -> None:
    print("---------")
    for row in field:
        print("| " + " ".join(row) + " |")
    print("---------")


def input_to_field(command: str) -> list:
    current = 0
    rows = 0
    field = [
        [_, _, _],
        [_, _, _],
        [_, _, _],
    ]
    for n in list(command):
        if n == X:
            symbol = X
        elif n == Z:
            symbol = Z
        else:
            symbol = _

        field[rows][current] = symbol
        current += 1
        if current == 3:
            current = 0
            rows += 1

    return field


# field0 = [
#     [X, Z, X],
#     [Z, _, Z],
#     [X, X, _],
# ]
#
# field1 = [
#     [X, Z, X],
#     [Z, X, Z],
#     [X, X, Z],
# ]

# print_field(field0)
# print('---')
# print_field(field1)

print("Enter cells:")
cells = input()

print_field(input_to_field(cells))

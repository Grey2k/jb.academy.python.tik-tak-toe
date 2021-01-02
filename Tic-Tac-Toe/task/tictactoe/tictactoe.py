from typing import Optional

# write your code here
# EXAMPLES:
#
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

X = 'X'
Z = 'O'
S = ' '

STATE_X_WINS = 'X wins'
STATE_O_WINS = 'O wins'
STATE_NOT_FINISHED = 'Game not finished'
STATE_DRAW = 'Draw'
STATE_IMPOSSIBLE = 'Impossible'

N = 3


def print_field(field_list: list) -> None:
    print("---------")
    for row in field_list:
        print("| " + " ".join(row) + " |")
    print("---------")


def input_to_field(command: str) -> list:
    current = 0
    rows = 0

    field_list = []

    for _ in range(N):
        field_list.append([S for _ in range(N)])

    for n in list(command):
        if n == X:
            symbol = X
        elif n == Z:
            symbol = Z
        else:
            symbol = S

        field_list[rows][current] = symbol
        current += 1
        if current == N:
            current = 0
            rows += 1

    return field_list


def is_impossible(field_list: list) -> bool:
    count_x = len([x for row in field_list for x in row if x == X])
    count_z = len([z for row in field_list for z in row if z == Z])

    if abs(count_x - count_z) not in [0, 1]:
        return True

    x_win = False
    z_win = False

    for i in range(N):
        # rows
        if len([v for v in field_list[i] if v == X]) == N or \
                len([row[i] for row in field_list if row[i] == X]) == N:
            x_win = True

        if len([v for v in field_list[i] if v == Z]) == N or \
                len([row[i] for row in field_list if row[i] == Z]) == N:
            z_win = True

    return (x_win is True) and (z_win is True)


def get_winner(field_list: list) -> Optional[str]:
    lr_x = 0
    lr_z = 0

    rl_x = 0
    rl_z = 0

    for i in range(N):
        # rows
        if len([v for v in field_list[i] if v == X]) == N or \
                len([row[i] for row in field_list if row[i] == X]) == N:
            return X

        if len([v for v in field_list[i] if v == Z]) == N or \
                len([row[i] for row in field_list if row[i] == Z]) == N:
            return Z

    for j in range(N):
        for k in range(N):
            if j == k:
                if field_list[j][k] == X:
                    lr_x += 1
                elif field_list[j][k] == Z:
                    lr_z += 1

            if (j + k) == (N - 1):
                if field_list[j][k] == X:
                    rl_x += 1
                elif field_list[j][k] == Z:
                    rl_z += 1

    if lr_x == N:
        return X
    elif lr_z == N:
        return Z
    elif rl_x == N:
        return X
    elif rl_z == N:
        return Z

    return None


def is_finished(field_list: list) -> bool:
    empties = len([s for row in field_list for s in row if s == S])

    return empties == 0


def game_state(field_list: list) -> str:
    if is_impossible(field_list):
        return STATE_IMPOSSIBLE

    winner = get_winner(field_list)

    if winner is not None:
        return STATE_X_WINS if winner == X else STATE_O_WINS

    return STATE_DRAW if is_finished(field_list) else STATE_NOT_FINISHED


def is_occupied(field_list: list, coord_x: int, coord_y: int) -> bool:
    try:
        if field_list[coord_x][coord_y] == S:
            return False
    except Exception as e:
        print('Exception: {}', e)
        return True

    return True


# print("Enter cells:")
# cells = input()
#
# field = input_to_field(cells)
# print_field(field)
# print(game_state(field))

field = input_to_field(S * (N ** 2))
current_plays = X
state = STATE_NOT_FINISHED

while True:
    print("Enter the coordinates:")

    try:
        x, y = [int(coord) - 1 for coord in input().split()]
    except ValueError:
        print('You should enter numbers!')
        continue

    if is_occupied(field, x, y):
        print('This cell is occupied! Choose another one!')
        continue

    field[x][y] = current_plays

    # change player
    current_plays = Z if current_plays == X else X
    print_field(field)

    state = game_state(field)

    if state == STATE_NOT_FINISHED:
        continue

    break

print(state)

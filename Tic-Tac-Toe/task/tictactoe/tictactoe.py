from typing import Optional

# write your code here

X = 'X'
Z = 'O'
S = '_'

STATE_X_WINS = 'X wins'
STATE_O_WINS = 'O wins'
STATE_NOT_FINISHED = 'Game not finished'
STATE_DRAW = 'Draw'
STATE_IMPOSSIBLE = 'Impossible'

N = 3


def print_field(field: list) -> None:
    print("---------")
    for row in field:
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

field = input_to_field(cells)
print_field(field)


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


def game_state(field_list: list):
    if is_impossible(field_list):
        return STATE_IMPOSSIBLE

    winner = get_winner(field_list)

    if winner is not None:
        return STATE_X_WINS if winner == X else STATE_O_WINS

    return STATE_DRAW if is_finished(field_list) else STATE_NOT_FINISHED


print(game_state(field))

height = int(input().strip())

SYMBOL = '#'
SPACE = ' '

# triangle width is 2n - 1
width = 2 * height - 1

for i in range(1, height + 1):
    level = i * 2 - 1
    spaces = (width - level) // 2

    print('{}{}{}'.format(spaces * SPACE, level * SYMBOL, spaces * SPACE))

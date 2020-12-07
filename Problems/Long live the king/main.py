x = int(input().strip()) - 1
y = int(input().strip()) - 1

limit = 7
moves = 8

if 1 <= x <= limit - 1 and 1 <= y <= limit - 1:
    print(moves)
elif x in (0, limit) and y in (0, limit):
    print(3)
else:
    print(5)

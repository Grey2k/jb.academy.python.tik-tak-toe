string = input().strip()

print([int(x) for x in list(string) if int(x) % 2 == 1])

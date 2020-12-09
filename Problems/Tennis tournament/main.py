n = int(input().strip())

games = []

for _ in range(n):
    games.append(input().strip().split())

wins = [game[0] for game in games if game[1] == 'win']

print(wins)
print(len(wins))

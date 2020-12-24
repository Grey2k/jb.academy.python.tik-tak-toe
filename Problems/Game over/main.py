scores = input().split()
# put your python code here

score = 0
lives = 3

for s in scores:
    if lives == 0:
        print('Game over')
        break

    if s == 'I':
        lives -= 1
        continue

    if s == 'C':
        score += 1
        continue
else:
    print('You won')

print(score)

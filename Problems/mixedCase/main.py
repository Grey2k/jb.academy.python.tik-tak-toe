words = input().lower().split()

result = []
for i, _ in enumerate(words):
    if i > 0:
        result.append(words[i].capitalize())
    else:
        result.append(words[i])

print(''.join(result))

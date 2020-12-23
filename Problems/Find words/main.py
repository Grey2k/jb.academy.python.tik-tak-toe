words = input().split()

found = []
for word in words:
    if word.endswith('s'):
        found.append(word)

print("_".join(found))

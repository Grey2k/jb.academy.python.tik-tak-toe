text = input()
words = text.split()

for word in words:
    if word.lower().startswith(('www.', 'http://', 'https://')):
        print(word)

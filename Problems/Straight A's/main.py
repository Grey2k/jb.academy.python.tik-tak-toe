# put your python code here
grades = input().split()

mark = 'A'

count = len([a for a in grades if a == mark])

print(round(count / len(grades), 2))

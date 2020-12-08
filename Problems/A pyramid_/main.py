n = 4
start = "'"
addition = '"\''

result = start
print(result)

for _ in range(n - 1):
    result += addition
    print(result)

n = int(input())

lucky = []

for _i in range(n):
    candidate = int(input().strip())

    if candidate % 7 == 0:
        lucky.append(candidate)

for each in lucky:
    print(each ** 2)

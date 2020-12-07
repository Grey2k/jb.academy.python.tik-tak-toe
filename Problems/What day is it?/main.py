timezone = int(input().strip())

point_minutes = 10 * 60 + 30
day_minutes = 24 * 60

current = 'Tuesday'
before = 'Monday'
after = 'Wednesday'

if point_minutes + (timezone * 60) < 0:
    print(before)
elif point_minutes + (timezone * 60) > day_minutes:
    print(after)
else:
    print(current)

score = float(input().strip())
maximum = float(input().strip())

A = 100.0
B = 90.0
C = 80.0
D = 70.0
F = 60.0

percent = score / maximum * 100

if B <= percent <= A:
    print('A')
elif C <= percent < B:
    print('B')
elif D <= percent < C:
    print('C')
elif F <= percent < D:
    print('D')
elif percent < F:
    print('F')

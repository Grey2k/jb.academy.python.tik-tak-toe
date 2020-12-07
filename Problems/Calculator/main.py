# put your python code here
first = float(input().strip())
second = float(input().strip())
operand = input().strip()

SUM = '+'
REDUCE = '-'
DIVIDE = '/'
MULTIPLY = '*'

MOD = 'mod'
POW = 'pow'
DIV = 'div'

if operand == SUM:
    print(sum([first, second]))
elif operand == REDUCE:
    print(first - second)
elif operand == DIVIDE and second != 0.0:
    print(first / second)
elif operand == MULTIPLY:
    print(first * second)
elif operand == MOD and second != 0.0:
    print(first % second)
elif operand == POW:
    print(first ** second)
elif operand == DIV and second != 0.0:
    print(first // second)
else:
    print("Division by 0!")

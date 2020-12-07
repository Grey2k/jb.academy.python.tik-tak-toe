score = float(input().strip())

if score < 2:
    print('Analytic')
elif 2 <= score <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')

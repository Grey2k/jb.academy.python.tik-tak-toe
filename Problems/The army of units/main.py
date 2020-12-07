count = int(input().strip())

if count < 1:
    print('no army')
elif 1 <= count <= 9:
    print('few')
elif 10 <= count <= 49:
    print('pack')
elif 50 <= count <= 499:
    print('horde')
elif 500 <= count <= 999:
    print('swarm')
else:
    print('legion')

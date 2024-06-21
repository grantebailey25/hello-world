print('Provide your desired top size:', end = ' ')
SIZE = int (input())
for i in range (0, SIZE):
    print(' ' * (SIZE - 1), end = '')
    print('||')
for i in range (0, SIZE):
    for j in range (0, SIZE - 1 - i):
        print(' ', end = '')
        j += 1
    for j in range (0, i):
        print('*', end = '')
        j += 1
    print('||', end = '')
    for j in range (0, i):
        print('*', end = '')
        j += 1
    print()
    i += 1
print('=' * SIZE * 2)
for i in range (0, SIZE):
    for j in range (0, i):
        print(' ', end = '')
        j += 1
    for j in range (0, SIZE - 1 - i):
        print('*', end = '')
        j += 1
    print('||', end = '')
    for j in range (0, SIZE - 1 - i):
        print('*', end = '')
        j += 1
    print()
    i += 1
for i in range (0, SIZE * 2):
    print(' ' * (SIZE - 1), end = '')
    print('||')
for i in range (0, SIZE):
    print('=' * SIZE * 2)
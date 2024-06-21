print('Provide your desired top size:', end = ' ')
SIZE = int (input())
for i in range (0, SIZE):
    print(' ' * (SIZE - 1), end = '')
    print('||')
for i in range (0, SIZE):
    print(' ' * (SIZE - 1 - i), end = '')
    print('*' * i, end = '')
    print('||', end = '')
    print('*' * i)
    i += 1
print('=' * SIZE * 2)
for i in range (0, SIZE):
    print(' ' * i, end = '')
    print('*' * (SIZE - 1 - i), end = '')
    print('||', end = '')
    print('*' * (SIZE - 1 - i))
    i += 1
for i in range (0, SIZE * 2):
    print(' ' * (SIZE - 1), end = '')
    print('||')
for i in range (0, SIZE):
    print('=' * SIZE * 2)

#Creating a function for the letter M
def m():
    print('M     M')
    print('MM   MM')
    print('M M M M')
    print('M  M  M')
    for i in range(0, 3):
        print('M     M\n')
#Creating a function for the letter I
def i():
    print('IIIII')
    i = 0
    while i < 5:
        print('  I  ')
        i += 1
    print('IIIII\n')
#Creating a function for the letter S
def s():
    print(' SSSSS')
    print('S     S')
    print('S')
    print(' SSSSS')
    print('      s')
    print('S     S')
    print(' SSSSS\n')
#Creating a function for the letter P
def p():
    print('PPPPPP')
    for i in range (0, 2):
        print('P     P')
    print('PPPPPP')
    for i in range (0, 3) :
        print('P')
    print()
#Printing the letters
m()
i()
for j in range (0, 2):
    for k in range(0, 2):
        s()
    i()
for j in range (0, 2):
    p()
i()
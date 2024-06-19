#Function for repeating lines
def repeatLines(line, count):
    for i in range (0, count):
        print(line)
#Creating a function for the letter M
def m():
    print('M     M')
    print('MM   MM')
    print('M M M M')
    print('M  M  M')
    repeatLines('M     M\n', 3)
#Creating a function for the letter I
def i():
    i5 = 'I' * 5
    print(i5)
    i = 0
    repeatLines('  I  ', 5)
    print(i5 + '\n')
#Creating a function for the letter S
def s():
    s5 = ' ' + 'S' * 5
    print(s5)
    print('S     S')
    print('S')
    print(s5)
    print('      S')
    print('S     S')
    print(s5 + '\n')
#Creating a function for the letter P
def p():
    p6 = 'P' * 6
    print(p6)
    repeatLines('P     P', 2)
    print(p6)
    repeatLines('P', 3)
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

print('How many days are in the month?', end = ' ')
numDays = int(input())
print('What day will be the first Sunday of the month?', end = ' ')
firstSunday = int(input())
print('  Sun    Mon    Tue    Wed    Thu    Fri    Sat')
for i in range (0, 7):
    print('+' + ('-' * 6), end = '')
print('+')
dayCount = 0
numBlanks = (8 - firstSunday) % 7
for i in range(0, numBlanks):
    print('|      ', end = '')
for i in range(1, 8 - numBlanks):
    stringI = str(i)
    print('|  ' + stringI + '   ', end = '')
    dayCount += 1
print('|')
spaces = 3
dayCount += 1
while dayCount <= numDays:
    for i in range (7):
        if dayCount > numDays:
            print('|      ', end = '')
        else:
            if dayCount >= 10:
                spaces = 2
            stringDayCount = str(dayCount)
            print('|  ' + stringDayCount + (' ' * spaces), end = '')
            dayCount += 1
    print('|')
for i in range (0, 7):
    print('+' + ('-' * 6), end = '')
print('+')

#After you complete this program, try to make it more efficient using lists
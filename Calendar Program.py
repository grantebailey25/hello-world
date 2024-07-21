def printHeader():
    weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    print('  ', end = '')
    for i in range (len(weekdays)):
        print(weekdays[i] + (' ' * 4), end = '')
    print()
    for _ in range (7):
        print('+' + ('-' * 6), end = '')
    print('+')
def firstWeek(dayCount):
    numBlanks = (8 - firstSunday) % 7
    for _ in range(0, numBlanks):
        print('|      ', end = '')
    for i in range(1, 8 - numBlanks):
        stringI = str(i)
        print('|  ' + stringI + '   ', end = '')
        dayCount = dayCount + 1
    print('|')
    return dayCount
def restOfMonth(dayCount, spaces):
    while dayCount <= numDays:
        for _ in range (7):
            if dayCount > numDays:
                print('|      ', end = '')
            else:
                if dayCount >= 10:
                    spaces = 2
                stringDayCount = str(dayCount)
                print('|  ' + stringDayCount + (' ' * spaces), end = '')
                dayCount += 1
        print('|')
def printBottomBorder():
    for _ in range (7):
        print('+' + ('-' * 6), end = '')
    print('+')
    
print('How many days are in the month?', end = ' ')
numDays = int(input())
print('What day will be the first Sunday of the month?', end = ' ')
firstSunday = int(input())
printHeader()
dayCount = 0
dayCount = firstWeek(dayCount)
spaces = 3
dayCount += 1
restOfMonth(dayCount, spaces)
printBottomBorder()

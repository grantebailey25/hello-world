print('Provide the initial position of the object: ', end = ' ')
s0 = float(input())
print('Provide the velocity position of the object: ', end = ' ')
v0 = float(input())
print('Provide the time the object spent traveling: ', end = ' ')
t = float(input())
print('Provide the acceleration of the object: ', end = ' ')
a = float(input())

position = str(s0 + v0 * t + 1/2 * a * t**2)

print('The object\'s position is: ' + position)
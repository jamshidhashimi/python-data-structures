fruits = {'apple', 'banana', 'orange'}
print(fruits)
# {'orange', 'apple', 'banana'}

colors = set(['red', 'green', 'blue'])
print(colors)
# {'green', 'blue', 'red'}

print(colors[1])
# TypeError: 'set' object is not subscriptable

for color in colors:
    print(color)
# blue
# green
# red

print('blue' in colors)
# true

colors.add('orange')
print(colors)
# {'red', 'blue', 'green', 'orange'}

colors.remove('blue')
print(colors)
# {'green', 'orange', 'red'}

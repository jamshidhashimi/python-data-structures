# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

point = (3, 4)
print(point)
# (3, 4)

colors = ('red', 'green', 'blue')
print(colors)
# ('red', 'green', 'blue')

print(colors[1])
# green

colors.append('orange')
# AttributeError: 'tuple' object has no attribute 'append'

colors.remove('blue')
# AttributeError: 'tuple' object has no attribute 'remove'
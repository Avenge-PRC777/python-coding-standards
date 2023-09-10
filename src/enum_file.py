from enum import Enum

class Color(Enum):
    RED = 'red'
    BLUE = 'blue'

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

for color in Color:
    print(color)

print(Color['RED'])

print(Color.RED == Color.RED)
print(Color.RED == Color.BLUE)

print(Color('red'))
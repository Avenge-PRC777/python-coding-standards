# Contents
- [Contents](#contents)
- [dataclasses](#dataclasses)


# dataclasses
dataclasses package provides **decorators and functions to use with classes that are meant for storing data and are not involved in creation of objects that change a lot**.

In a class, one has to write __init__ and __repr__ functions. But dataclasses has decorator where you write code only having your variables and the decorator generates those functions.

```python
# Normal Class
class PointNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'PointNormal(x={self.x}, y={self.y})'

p1 = Point(1, 2)
print(p1)  # This will print: Point(x=1, y=2)

# dataclass Class
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
p2 = Point(3, 4)
print(p2)  # This will also print: Point(x=3, y=4)
```
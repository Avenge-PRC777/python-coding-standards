# Contents
- [Contents](#contents)
- [What is enum](#what-is-enum)
- [Where to use Enum](#where-to-use-enum)


# What is enum
Enums/enumerations are used to denote a set of options or choices. Enum is a set of values.

```python
from enum import Enum

class Color(Enum):
    RED = 'red'
    BLUE = 'blue'

# Color is an Enum here that has 2 Enum members: Color.RED and Color.BLUE

print(Color.RED) # Unlike normal class that would print value Color.RED is an Enum object which is printed as it is.
print(Color.RED.name) # Name of the Enum member's variable 'RED'
print(Color.RED.value) # Value of the Enum member: 'red'

for color in Color:
    print(color) # We can iterature thru an Enum to get all Enum members, this prints Color.RED, Color.BLUE, ...

print(Color['RED']) # This prints the Enum member based on variable name: Color.RED
print(Color('red')) # This prints the Enum member based on value name: Color.RED

print(Color.RED == Color.RED) # True
print(Color.RED == Color.BLUE) # False
```

# Where to use Enum

```python
### Way 1
from enum import Enum

# Define an enumeration for days of the week
class DaysOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

# You can now use the DaysOfWeek enumeration
today = DaysOfWeek.WEDNESDAY
if today == DaysOfWeek.WEDNESDAY:
    print("It's a weekday!")

### Way 2
today = "Wednesday"

# Checking for equality
if today == "Wednesday":
    print("It's a weekday!")
```

In way 1, it is very clear, today is DaysOfWeek's Wednesday whereas in Way 2 its a variable that can have typos, changes. Way 1 is more self-explanatory that we are looking at a day of week.
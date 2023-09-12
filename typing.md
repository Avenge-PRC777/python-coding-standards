# Contents
- [Contents](#contents)
- [typing](#typing)
  - [type-hinting](#type-hinting)
    - [basic syntax](#basic-syntax)
    - [classes can also be used to type hint](#classes-can-also-be-used-to-type-hint)
    - [when your function does not return anything](#when-your-function-does-not-return-anything)
  - [typing package](#typing-package)


# typing
Before going to typing, understanding type hinting.

## type-hinting

It is the process of adding data type information to variables, function outputs so that developers can know better variable is supposed to have what type. It is just a standard and not a rule.

Meaning **if you type hint a variable as int and give it a value of string, there will not be any error. type-hinting is just hinting.**

### basic syntax

How it happens:
1. We just add **: type** to a variable
2. We just add **-> type** to function before definition ends (that is before colon)

```python
# Normal function
def greet(name = "Guest", age = 30):
    return f"Hello, {name}! You are {age} years old."

# Function with type hinting
def greet(name: str = "Guest", age: int = 30) -> str:
    return f"Hello, {name}! You are {age} years old."
```

### classes can also be used to type hint
```python
class CustomDataType:
    value: str = "Hey"
    def __init__(self, value: str):
        self.value = value

def use_custom_data_type(obj: CustomDataType) -> CustomDataType:
    return obj
```

### when your function does not return anything
None is used as return type
```python
def print_val(val:str = 3) -> None:
```

## typing package

typing is a package that provides type hints for data types that are not basic for example list.

```python
from typing import List, Tuple, Dict, Any, Optional

def process_list(lst: List[int]) -> List[int]:
# This means the function accepts a list datatype whose values are integers and also returns a similar list

def process_tuple(tple: Tuple[float, float]) -> None:
# Function accepts a tuple datatype whose values are floats

def process_dict(dct: Dict[str, int]) -> None:
# Function accepts a dictionary datatype whose key value pairs are of type string and integer

def process_data(data: Any) -> None:
# Indicates data can have "any datatype", as we are not sure beforehand what value it can have, maybe its coming from multiple functions

def process_data(data: Optional[str]) -> None:
# This means the datatype of data can be either string or None. The datatype of the variable (and not the variable itself) is optional.
```
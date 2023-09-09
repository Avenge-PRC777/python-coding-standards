# python-coding-standards
Contains information on how to write modular, clean, standard python code

# Contents
- [python-coding-standards](#python-coding-standards)
- [Contents](#contents)
- [Configuration based design](#configuration-based-design)
  - [Why config based design](#why-config-based-design)
  - [How should the design be](#how-should-the-design-be)
  - [Ways to implement such a design](#ways-to-implement-such-a-design)
  - [What kind of classes are available](#what-kind-of-classes-are-available)
  - [What class should we go for](#what-class-should-we-go-for)
  - [How to implement a static class in python](#how-to-implement-a-static-class-in-python)
    - [A bit about decorators.](#a-bit-about-decorators)
    - [@staticmethod decorator](#staticmethod-decorator)
    - [How to use a static class for config then finally](#how-to-use-a-static-class-for-config-then-finally)
- [enum](#enum)


# Configuration based design

## Why config based design
When our codebase has multiple parameters that can be changed by different users in different ways, by end users or other developers, and **we dont want to alter code everytime as thats not scalable**, configuration based design is a beneficial practice.

Configuration can also help the codebase in following ways:
- **Be scalable**: adjusting resource parameters
- **Documentation**: a json can be self-serve way of know what input options are available
- **Maintenance and testing**: Very less changes might be required to maintain or test as most things can be done by playing around with config.

## How should the design be

In a codebase, some or other component like a function may need some parameter value from config.

**So, one design is to make the config values available to all files and functions.**

## Ways to implement such a design

1. Read the file contents into a variable and keep sending the variable to all functions that would need to use a value like say *"args.Name"*.
2. Read the file contents into a global variable and import the variable everywhere to use. **Yes we can import variables too from files**:
```
# file.py
import random
variable = 3
def main(): ...

# other.py
from file import variable
print(variable) # will print 3
```
3. Use a class to represent a configuration

Now, personally I have seen the following:

1. Approach 1 usually yeilds unclean code as you have to always keep passing the config variable into every function and its subfunctions.
2. Approach 2 can lead to global variable pollution (tracking state, unpredictable testing as a function using global variable can have a invisibile dependency on another function using same global variable); also again it's a variable, though imported now, access to parameters will be mostly thru dictionary key value which makes the code not very readable.
```
# code 1
from config import Config
load(Config.dataset)

# code 2
from main import config
load(config["dataset"])

# code 1 has better clarity in terms that a configuration class has more probability of having config related stuff than a simple config variable.
```
3. Approach 3 is a good solution.

## What kind of classes are available

Static class or instance class or singleton class?

Instances are required when we need objects with different states (of variables say) or 1 object can having changing state throught the program (example car object with speed variable)

1. Static class: No need of creating instances/objects of class. Direct access to class and its properties. Mostly used as utility classes.
2. Instance class: Object of class must be created.
3. Singleton class: A specific case of instance class where one instance is created in runtime that is made available to all functions at runtime. **Any changes to state (properties) of this object reflect across the application globally as this is one and only available object of the class**

## What class should we go for
If an instance is created for configuration, that has to be passed again in every function just like variable approach 1.

**That means, we go for static class when implementing Configuration.**

## How to implement a static class in python

As such there is no built in way of static class in python like we have in JAVA (public static ClassName, for example), **we can define staticness at function level thru decorator**.

### A bit about decorators.

1. Decorators are functions too.
2. They just modify/decorate another function (add something before and/or after the function)
3. **If you define a function def func():, then func variable contains reference to the FUNCTION OBJECT i.e., its memory location which is called by adding "()"**. A normal class object may not be callable wherease a function object also just an object is just callable. This is crucial in understanding how decorator works.

```
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello() # Here since function is a decorated function, the decorator is called as "my_decorator(say_hello)()". It takes input the function object and outputs a function object.
```

### @staticmethod decorator
For a class, we can have a method with @staticmethod decorator that will make it static. **Static methods can't access class variables directly but indirectly thru class name**

```
# Normal class method
class X:
    a=3
    def my_fun(self, a=3):
        self.a=a

# Static class method
class X:
    a=3
    @staticmethod
    def my_fun(a=3):
        X.a = a
```

### How to use a static class for config then finally

Let's say your config file has the static class. Just load config to this class in the entrypoint file and then just import the class everywhere else to use the values.
```
# main.py
from config import Config, set_config
config_data = read_config(args.config_file)
set_config(config_data)

# subsequent_file.py
from config import Config
load_data(Config.dataset_path)
```

Refer to **config.py**.

# enum
[Go to file](enum.md)
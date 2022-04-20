# *args: Many Positional Arguments

def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(2, 3, 5))
print(add(2, 3, 6, 8, 7, 4, 21))


# **kwargs: Many Keyword Arguments
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") # get will return none if make does not exist
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)
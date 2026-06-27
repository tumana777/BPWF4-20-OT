# class Student:
#     course = "Python"
#     status_active = True
#
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __add__(self, other):
#         return "I am working when + operator is used"
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_email(self, domain):
#         return f"{self.first_name}.{self.last_name}@{domain}"
#
#     def __repr__(self):
#         return f"Student('{self.first_name}', '{self.last_name}', {self.age})"
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name} is {self.age} years old"
#
# st1 = Student("Otar", "Tumanishvili", 35)
# st2 = Student("Nino", "Aleqsidze", 25)

# print(type(st1))
# print(type(st2))

# tup = (2, 6)
# tup1 = (1, 2, 3, 4, 5)
#
# print(tup1 + tup)


# print(st1 + st2)

# class Parent:
#     pass
#
#
# class Vector(Parent):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return f"{other} is not a Vector object"
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         return Vector(self.x * other, self.y * other)
#
#     def __truediv__(self, other):
#         return Vector(self.x / other, self.y / other)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)

# v1.__mul__(v2, 5)

# print(v1 + v2)
# print(v1 - v2)
# print(v1 * 2)
# print(v1 / 2)


# print(isinstance(v1, object))
# print(isinstance(True, bool))
# print(isinstance(True, int))


# class Test:
#     def __new__(cls):
#         print("I am __new__ method")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("I am __init__ method")
#
# t = Test()


# class Test:
#     def __new__(cls, a, b):
#         print("I am __new__ method")
#         return super().__new__(cls)
#
#     def __init__(self, a, b):
#         print("I am __init__ method")
#
# t = Test(1, 2)


# class Test:
#     def __init__(self):
#         print("I am __init__ method")
#
#     def show(self):
#         print("I am show method")
#
# t = Test()

# def test():
#     print("I am test function")
#
# print(callable(test))

# class Multiplier:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self):
#         print("I am callable object")
#
# x = Multiplier(5)
#
# x()

# class Multiplier:
#     def __init__(self, a):
#         self.a = a
#
#     def __call__(self, b):
#         return self.a * b
#
# multiplier_by_2 = Multiplier(2)
# multiplier_by_3 = Multiplier(3)
#
# print(multiplier_by_2(5))
# print(multiplier_by_3(5))

# class Parent:
#     pass
#
# class MyMeta(type):
#     def __new__(mcls, name, bases, attrs):
#         print(f"mcls: {mcls}")
#         print(f"name: {name}")
#         print(f"bases: {bases}")
#         attrs["created_at"] = "Admin"
#         print(f"attrs: {attrs}")
#
#         return super().__new__(mcls, name, bases, attrs)
#
# class MyClass(Parent, metaclass=MyMeta):
#     x = 5
#     y = 10
#
#     def test(self):
#         return "test"
#
# my_class = MyClass()
#
# print(my_class.created_at)

# def change_value(func):
#     def wrapper(x, y):
#         x += 2
#         y += 2
#         return func(x, y)
#     return wrapper
#
# @change_value
# def test(a, b):
#     print(f"a={a}, b={b}")
#
# test(5, 7)

import time


# def test():
#     start_time = time.time()
#     print("Function execution started...")
#     time.sleep(2)
#     print("Function execution finished...")
#     end_time = time.time()
#     print(f"Execution time: {end_time - start_time} seconds")
#
# test()


def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Function execution time: {end_time - start_time:.2f} seconds")
    return wrapper


# @time_counter
# def test():
#     input("Please press enter to continue...")
#
# test()

@time_counter
def test(n):
    time.sleep(n)

test(8)
























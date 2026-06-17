# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Alex', 'white', 35),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# while True:
#     name = input("Please enter a name: ")
#
#     found_list = []
#
#     for person in persons:
#         if name == person[0]:
#             found_list.append(person)
#
#     if found_list:
#         last_name = input("Please enter a last name: ")
#
#         for person in found_list:
#             if last_name == person[1]:
#                 print(f"Found {person[0]} {person[1]} with age {person[2]}")
#         else:
#             print("Last name not found")
#     else:
#         print("Name Not found")


# def add(a, b):
#     return a + b
#
# print(add(5, 7))

# def add(*a):
#     total = 0
#
#     for i in a:
#         total += i
#
#     print(total)
#
# add(5, 7, 9, 11)


# def add(*args):
#     return sum(args)
#
# print(add(5, 7, 9, 11))


# def test(a, b, *args):
#     return f"a={a}, b={b}, args={args}"
#
# print(test("test", "test2", "test3", "test4", "test5"))


# a = "test"
#
# print(tuple(a))

# def test(a, b, *args):
#     return f"a={a}, b={b}, args={args}"
#
# print(test("test", "test5", "test6", "test7", "test8"))


# a, *b, c = 1, 2, 3
#
# print(a)
# print(b)
# print(c)


# def test(a, b):
#     return f"a={a}, b={b}"

# iter_obj = [5, 8]
# iter_obj = (5, 8)
# iter_obj = "hi"
# iter_obj = {"Hello", "World"}

# print(test(*iter_obj))


# def greet(name, greeting="Hello"):
#     return f"{greeting} {name}!"
#
# print(greet("Otar"))

# def greet(name="User", greeting="Hello"):
#     return f"{greeting} {name}!"
#
# print(greet(greeting="Hi"))


# def greet(name, greeting):
#     return f"{greeting} {name}!"
#
# print(greet(greeting="Hi", name="Otar"))


# def greet(name="User", greeting="Hello"):
#     return f"{greeting} {name}!"
#
# print(greet(greeting="Hi", name="Otar"))

# def greet(name, greeting, age):
#     return f"{greeting} {name}, you are {age} years old!"
#
# print(greet("Otar", "Hi", age=35))


# def test(a, b=9, *args):
#     return f"a={a}, args={args}, b={b}"
#
#
# print(test(1, 2, 3, 4, 5, 6))


# def test(a, b=6, *args, **kwargs):
#     return f"a={a}, b={b}, args={args}, kwargs={kwargs}"
#
# print(test("Otar", "test", age=35, gender="Male"))

# a = 10 # Global variable
#
# def outer():
#     a = 8 # Enclosing variable
#
#     def inner():
#         a = 6 # Local variable
#
#         return a
#
#     return inner()
#
# print(outer())


# __name__ = "Global"
#
# def outer():
#     __name__ = "Enclosing"
#
#     def inner():
#         __name__ = "Local"
#         return __name__
#
#     return inner()
#
# print(outer())

# def test(*args, a):
#     return f"args={args}"
#
# print(test("test", "test5", "test6", "test7", a="test8"))


















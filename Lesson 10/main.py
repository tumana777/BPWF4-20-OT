# def add(a, b):
#     return a + b
#
# result = add(5, 7)
# result = result + add(10, 12)
#
# print(result)

# def add(a, b):
#     return a + b
#
# result = add
#
# print(result)

# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     return a / b
#
#
# def test(func, y, z):
#     if callable(func):
#         return func(y, z)
#     return "Not callable argument!"


# print(test(add, 5, 7))
# print(test(sub, 5, 7))
# print(test(mul, 5, 7))
# print(test(div, 5, 2))

# print(callable(add))
# print(callable(input))
# print(callable(str))


# print(test(add, 8, 9))
#
# print("Hello World")


# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def mul(a, b):
#     return a * b
#
# def div(a, b):
#     return a / b
#
#
# def test(func, y, z):
#     if callable(func):
#         return func(y, z)
#     return "Not callable argument!"
#
# func_list = [add, sub, mul, div, 89]
#
# for func in func_list:
#     print(test(func, 14, 7))


# def get_multiplier(a):
#
#     def multiply(b):
#         return a * b
#
#     return multiply
#
# multiplier_by_2 = get_multiplier(2)
# multiplier_by_3 = get_multiplier(3)
#
# print(multiplier_by_2(5))
# print(multiplier_by_2(7))
# print(multiplier_by_3(5))
# print(multiplier_by_3(7))


# def test():
#     return test()
#
# test()

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#
#     if n < 0:
#         return "Factorial is not defined for negative numbers!"
#
#     return n * factorial(n - 1) # 5 * 4 * 3 * 2 * 1
#
# print(factorial(-5))

# x = lambda a, b: a + b

# x = lambda a: a * 2
#
# print(x(5))

# x = lambda a, b: a - b if a > b else b - a
#
# print(x(9, 3))

# names = ["otar", "ana", "john", "aLex", "dAvit", "sandro"]


# def change_name(name):
#     return name.capitalize()

# names = list(map(lambda x: x.capitalize(), names))
#
# print(names)

# names = ["otar", "ana", "john", "aLex", "dAvit", "sandro"]
#
# long_names = list(filter(lambda x: len(x) > 4, names))
#
# print(long_names)


# names = ["otar", "ana", "john", "aLex", "dAvit", "sandro"]

# from functools import reduce
#
# numbers = [4, 5, 6, 7, 8, 9, 10]
#
# x = reduce(lambda a, b: a + b, numbers)
#
# print(x)


# names = ["otar", "ana", "John", "aLex", "dAvit", "sandro"]

# sorted_names = sorted(names)
# sorted_names = sorted(names, key=lambda x: len(x), reverse=True)
#
# print(sorted_names)



# try:
#     a = int(input("Enter number1: "))
#     b = int(input("Enter number2: "))
#
#     print(a / b)
# except ValueError:
#     print("Text not allowed")
# except ZeroDivisionError:
#     print("Can not divide by zero")
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print("No error")
# finally:
#     print("Program ended")
















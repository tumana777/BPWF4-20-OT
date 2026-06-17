# def add_numbers(number=5):
#     pass
#
#
# print(add_numbers(3))

# def test(*args):
#     pass
#
# print(test(1, 8))

# import string
#
# print(string.punctuation)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.ascii_letters)

# def count_words(text):
#     my_dict = {}
#
#     for word in text.split():
#         word = word.strip(string.punctuation).lower()
#         if word in my_dict:
#             my_dict[word] += 1
#         else:
#             my_dict[word] = 1
#     return my_dict


# print(count_words("This is a test, This test is fun, this is also another test."))


# file = open("test/test.txt", "r")
#
# print(file.read())
#
# file.close()

# file = open("../Lesson 10/main.py", "r")
#
# print(file.read())
#
# file.close()

# file = open("test.txt", "r")
#
# data = file.read(15)
#
# file.close()
#
# print(data)


# file = open("test.txt", "r")
#
# data1 = file.read(15)
# data2 = file.read()
#
# file.close()
#
# print(data2)


# file = open("test.txt", "r")
#
# data1 = file.read()
# file.seek(0)
# data2 = file.read()
#
# file.close()
#
# print(data1)
# print(data2)


# file = open("test.txt", "r")
#
# data1 = file.read()
#
# file.close()
#
# print(type(data1))

# file = open("test.txt", "r")
#
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# line4 = file.readline()
#
# file.close()
#
# print(line1)
# print(line2)
# print(line3)
# print(line4)


# file = open("test.txt", "r")
#
# lines = file.readlines()
#
# file.close()
#
# print(lines)

# file = open("test.txt", "r")
#
# print(file.readable())
#
# file.close()

# file = open("test1.txt", "x")
#
# print(file.writable())
#
# file.close()

# file = open("test2.txt", "w")
#
# print(file.writable())
# print(file.readable())
#
# file.close()


# file = open("test1.txt", "w")
#
# file.write("Hello World\n")
# file.write("This is a test")
#
# file.close()


# file = open("test1.txt", "a")
#
# file.write("\nThis is another test\n")
#
# file.close()

# names = ["Otar", "Nino", "Alex", "John"]
#
# file = open("names.txt", "w")
#
# for name in names:
#     file.write(f"{name}\n")
#
# file.close()


# names = ["Otar", "Nino", "Alex", "John"]
#
# new_names = [f"{name}\n" for name in names]
#
# file = open("names.txt", "w")
#
# file.writelines(new_names)
#
# file.close()


# file = open("names.txt", "w+")
#
# print(file.readable())
# print(file.writable())
#
# file.close()


with open("test1.txt", "r") as file:
    data = file.read()



print(data)












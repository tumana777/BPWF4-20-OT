import csv
import os

# print(os.getcwd())
# print(os.listdir())
# print(os.path.abspath("main.py"))

# print(os.path.exists("test.txt"))

# print(os.path.isfile("main.py"))
# print(os.path.isfile("test"))

# if os.path.exists("test"):
#     print("Directory exists")
# else:
#     os.mkdir("test")

# if os.path.exists("test"):
#     os.rmdir("test")
# else:
#     print("Directory does not exist")

# print(os.path.join("test", "test.txt"))

# if os.path.exists("text.txt"):
#     os.remove("text.txt")
# else:
#     print("File does not exist")

# os.rename("text.txt", "test/test.txt")

import shutil

# shutil.rmtree("test")

# name = "Otar"
#
# encoded_name = name.encode("utf-8")

# print(encoded_name)
# print(type(encoded_name))

# with open("name.bin", "wb") as file:
#     file.write(encoded_name)
#
# with open("name.bin", "rb") as file:
#     data = file.read()
#
# decoded_name = data.decode()
#
# print(decoded_name)
# print(type(decoded_name))

# name = "ოთარ"
#
# encoded_name = name.encode("utf-8")
#
# with open("new_name.bin", "wb") as file:
#     file.write(encoded_name)

# with open("new_name.bin", "rb") as file:
#     data = file.read()
#
# print(type(data))


# import csv
#
# with open("companies.csv", "r") as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# headers = ["name", "age", "email"]
#
# data1 = ["Otar", 35, "test@gmail.com"]
# data2 = ["Nini", 25, "test1@gmail.com"]
#
# with open("names.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)
#     writer.writerow(data1)
#     writer.writerow(data2)

# headers = ["name", "age", "email"]
#
# persons = [
#     ["Otar", 35, "test@gmail.com"],
#     ["Nini", 25, "test1@gmail.com"],
#     ["Ana", 37, "test1@gmail.com"],
#     ["Alex", 87, "test1@gmail.com"]
# ]
#
# with open("names1.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(headers)
#     writer.writerows(persons)

# with open("companies.csv", "r") as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print(row)

# headers = ["name", "age", "email"]
#
# data = [
#     {"name": "Otar", "age": 35, "email": "ot@gmail.com"},
#     {"name": "Davit", "age": 27, "email": "dv@gmail.com"},
#     {"name": "Levan", "age": 34, "email": "lv@gmail.com"}
# ]
#
# with open("names.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(data)


# headers = ["name", "age", "email"]

# data = [
#     {"name": "Otar", "age": 35, "email": "ot@gmail.com"},
#     {"name": "Davit", "age": 27, "email": "dv@gmail.com"},
#     {"name": "Levan", "age": 34, "email": "lv@gmail.com"}
# ]

# headers = data[0].keys()
#
# with open("names.csv", "w") as file:
#     writer = csv.DictWriter(file, fieldnames=headers)
#     writer.writeheader()
#     writer.writerows(data)


# import faker
#
# fake = faker.Faker()

# print(fake.name())
# print(fake.address())
# print(fake.email())
# print(fake.phone_number())
# print(fake.first_name())
# print(fake.last_name())

# print(fake.company())
# print(fake.job())
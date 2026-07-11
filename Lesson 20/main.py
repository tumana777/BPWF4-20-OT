# student = {
#     "name": "Otar",
#     "age": 35,
#     "grades": [10, 9, 8, 7, 6],
#     "floated": 3.14,
#     "is_student": True,
#     "is_teacher": False,
#     "nothing": None,
#     "address": "Tbilisi",
#     "subjects": {"math": 10, "english": 9, "history": 8, "geography": 7, "chemistry": 6},
#     "friends": ("Nino", "Nikita", "Nikolay")
# }

# import json
#
# serialized_student = json.dumps(student, indent=4)

# print(serialized_student)
# print(type(serialized_student))

# deserialized_student = json.loads(serialized_student)
# print(deserialized_student)
# print(type(deserialized_student))

# import json
# from datetime import datetime
#
# student = {
#     "name": "Otar",
#     "age": 35,
#     "grades": [10, 9, 8, 7, 6],
#     "floated": 3.14,
#     "is_student": True,
#     "is_teacher": False,
#     "nothing": None,
#     "address": "Tbilisi",
#     "subjects": {"math": 10, "english": 9, "history": 8, "geography": 7, "chemistry": 6},
#     "friends": ("Nino", "Nikita", "Nikolay")
# }
#
# student2 = {
#     "name": "Nino",
#     "age": 25,
#     "grades": [10, 9, 8, 7, 6],
#     "floated": 3.14,
#     "is_student": True,
#     "is_teacher": False,
#     "nothing": None,
#     "address": "Tbilisi",
#     "subjects": {"math": 10, "english": 9, "history": 8, "geography": 7, "chemistry": 6},
#     "friends": ("Otar", "Nikita", "Nikolay")
# }
#
# students = [student, student2]
#
# data = {
#     "total_students": len(students),
#     "students": students,
#     "last_update": str(datetime.now())
# }
#
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4)


# import json
#
# with open("students.json", "r") as f:
#     data = json.load(f)
#
#
# print(type(data))

import json

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"

# st1 = Student("Tamar", 25)

# def student_serializer(obj):
#     return {
#         "name": obj.name,
#         "age": obj.age
#     }

# serialized_student = student_serializer(st1)

# with open("student.json", "w") as f:
#     json.dump(st1, f, indent=4, default=student_serializer)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"


# def student_deserializer(obj):
#     return Student(obj["name"], obj["age"])
#
# with open("student.json", "r") as f:
#     data = json.load(f, object_hook=student_deserializer)
#
# print(data)

import pickle

# student = {
#     "name": "Otar",
#     "age": 35,
#     "grades": [10, 9, 8, 7, 6],
#     "floated": 3.14,
#     "is_student": True,
#     "is_teacher": False,
#     "nothing": None,
#     "address": "Tbilisi",
#     "subjects": {"math": 10, "english": 9, "history": 8, "geography": 7, "chemistry": 6},
#     "friends": ("Nino", "Nikita", "Nikolay")
# }

# serialized_student = pickle.dumps(student)

# print(type(serialized_student))
# print(serialized_student)

# deserialized_student = pickle.loads(serialized_student)
#
# print(deserialized_student)


# with open("student.bin", "wb") as f:
#     pickle.dump(student, f)

# with open("student.bin", "rb") as f:
#     data = pickle.load(f)
#
# print(data)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"

# st1 = Student("Tamar", 25)


# with open("student.bin", "wb") as f:
#     pickle.dump(st1, f)


# with open("student.bin", "rb") as f:
#     data = pickle.load(f)
#
# print(data)

# import requests
#
# url = "https://jsonplaceholder.typicode.com/users"

# response = requests.get(url)

# print(response.status_code)
# data = response.json()

# for user in data:
#     print(type(user))

# print(response.text)
# print(response.content)
# print(response.headers)
# print(response)

import requests

url = "https://jsonplaceholder.typicode.com/users/5"

student = {
    "name": "Otar",
    "age": 35,
    "grades": [10, 9, 8, 7, 6],
    "floated": 3.14,
    "is_student": True,
    "is_teacher": False,
    "nothing": None,
    "address": "Tbilisi",
    "subjects": {"math": 10, "english": 9, "history": 8, "geography": 7, "chemistry": 6},
    "friends": ("Nino", "Nikita", "Nikolay")
}

response = requests.delete(url, json=student)

print(response.status_code)


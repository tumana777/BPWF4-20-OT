from pymongo import MongoClient
from faker import Faker
from random import randint

fake = Faker()

client = MongoClient("mongodb://localhost:27017/")

# print(client.list_database_names())

db  = client["BPWF4-20-OT"]

students = db["students"]

# print(students.count_documents({}))

# student = {
#     "name": "Otar",
#     "surname": "Aleqsidze",
#     "age": 25,
#     "course": "Python"
# }
#
# students.insert_one(student)

# students_list = [{'first_name': fake.first_name(), "last_name": fake.last_name(), "age": randint(10, 30)} for _ in range(5)]
#
# students.insert_many(students_list)

# print(students.find_one({"age": 25}))
# print(students.find_one({"first_name": "gvanca"}))

# for student in students.find():
#     print(student)

# for student in students.find({"name": "Otar"}):
#     print(student)

# for student in students.find({"age": 21}):
#     print(student)

# for student in students.find({"name": "Otar", "age": 35}):
#     print(student)

# for student in students.find({"age": {"$gt": 21}}):
#     print(student)

# for student in students.find({"age": {"$gte": 21}}):
#     print(student)

# for student in students.find({"age": {"$lt": 21}}):
#     print(student)

# for student in students.find({"age": {"$lte": 21}}):
#     print(student)

# for student in students.find({"age": {"$gt": 21, "$lt": 30}}):
#     print(student)

# for student in students.find({"age": {"$in": [21, 25, 30]}}):
#     print(student)

# for student in students.find({"age": {"$nin": [21, 25, 30]}}):
#     print(student)

# for student in students.find({"age": {"$ne": 25}}):
#     print(student)

# for student in students.find({"$and": [{"age": 25}, {"name": "giorgi"}]}):
#     print(student)

# students.update_one({}, {"$set": {"age": 30}})

# students.update_one({"first_name": "gvanca"}, {"$set": {"age": 30}})

# students.update_many({"first_name": "gvanca"}, {"$set": {"age": 35}})

# students.update_many({}, {"$set": {"info": "I am a student", "course": "Python"}})

# students.delete_one({})

# students.delete_many({"first_name": "gvanca"})

# students.delete_many({"name": "Otar", "age": 25})

# students.delete_many({})

# students.drop()










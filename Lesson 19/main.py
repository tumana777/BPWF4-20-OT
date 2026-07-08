# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# new_list = [str(num) for num in nums_list]
#
# nums = ", ".join(new_list)

# print(nums)

# with open("nums.txt", "w") as file:
#     file.write(nums)

# with open("nums.txt", "r") as file:
#     data = file.read()
#
# my_list = data.split(", ")
#
# nums_list = [int(char) for char in my_list]
#
# print(nums_list)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p1 = Person("Otar", 35)

def person_serializer(obj):

    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age
        }

    return f"{obj} is not a Person object"

serialized_person = person_serializer(p1)


def person_deserializer(obj):
    if isinstance(obj, dict):
        return Person(obj["name"], obj["age"])

    return f"{obj} is not a dict"


person = person_deserializer(serialized_person)

print(person)

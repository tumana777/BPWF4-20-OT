# empty_dict = {}

# print(empty_dict)

# print(type(empty_dict))

# empty_dict = dict()
#
# print(empty_dict)
#
# print(type(empty_dict))

# person = {"name": "Otar", "age": 35, "city": "Tbilisi"}

# names = ["Otar", "Nino", "Ana", "Alex", "John"]
# cities = ["Tbilisi", "Kutaisi", "Burgas", "Sofia", "Plovdiv"]
# ages = [35, 25, 20, 22, 30]
#
# for i in range(len(names)):
#     print(f"{names[i]} lives in {cities[i]} and is {ages[i]} years old.")


# persons = {
#     "Otar": 35,
#     "Nino": 25,
#     "Ana": 25,
#     "Alex": 22,
#     "John": 30,
#     "Ana": 20
# }
#
# print(persons)


# my_dict = {
#     "name": "Otar",
#     1:  "This is an integer",
#     3.14: "This is a float",
#     True: "This is a boolean",
#     None: "This is a None"
# }
#
# print(my_dict)


# my_dict = {
#     "str": "Otar",
#     "int": 35,
#     "list": [1 , 2, 3, 4, 5],
#     "float": 3.14,
#     "bool": True,
#     "none": None,
#     "dict": {"name": "Otar", "age": 35}
# }
#
# print(my_dict)

# persons = {
#     "Otar": 35,
#     "Nino": 25,
#     "Ana": 25,
#     "Alex": 22,
#     "John": 30,
#     "Walter": 55,
#     "Bob": 37
# }

# print(len(persons))

# print(persons["Otar"])
# print(persons["Walter"])
# print(persons["jon"])

# persons["Otar"] = 36
# persons["Jonny"] = 36
#
# print(persons["Jonny"])

# print(persons)


# persons = {
#     "Otar": 35,
#     "Nino": 25,
#     "Ana": 25,
#     "Alex": 22,
#     "John": 30,
#     "Walter": 55,
#     "Bob": 37
# }

# persons.pop("Otar")
# persons.popitem()

# persons.setdefault("Bob", 36)

# print(persons)

# for key in persons:
#     print(f"{key} is {persons[key]} years old.")

# print(persons.get("otar", "Not found"))

# print(list(persons.keys()))
# print(list(persons.values()))
# print(list(persons.items()))

# new_dict = {
#     "Jonny": 36,
#     "Bobby": 37,
#     "Walter1": 55
# }
#
# persons.update(new_dict)

#
# names = ["Otar", "Nino", "Ana", "Alex", "John"]
#
#
# my_dict = dict().fromkeys(names)
#
#
# print(my_dict)


# products = {
#     "Electonics": {
#         "TV": {"Samsung": {"title": "Samsung TV", "price": 1000}},
#         "AC": {"Samsung": {"title": "Samsung AC", "price": 1500}},
#         "Refrigerator": {"Midea": {"title": "Midea Refrigerator", "price": 2000}}
#     },
#     "Clothes": {
#         "Shirt": {"Nike": {"title": "Nike Shirt", "price": 400}},
#         "Pants": {"Puma": {"title": "Puma Pants", "price": 30}}
#     }
# }
#
# print(products["Electonics"]["AC"]["Samsung"]["price"])


# my_dict = {i: "test" for i in range(1, 6)}
#
# print(my_dict)
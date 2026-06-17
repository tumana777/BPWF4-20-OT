# lst1 = []

# print(len(lst1))

# print(lst1)

# print(type(lst1))

# lst2 = list()
#
# print(lst2)

# int_lst = [1, 2, 3, 4, 5]

# names = ["Otar", "Nino", "Alex", "John"]

# mixed_lst = [1, "Otar", 3.14, True, False, None, [1, 2, 3], "Hello World"]

# print(len(mixed_lst))

# nested_lst = [1, 2, 3, [4, 5, 6], 7, 8, 9]
#
# print(len(nested_lst))

# mixed_lst = [1, "Otar", 3.14, True, False, None, [1, 2, 3], "Hello World"]

# print(mixed_lst[0])
# print(mixed_lst[4])
# print(mixed_lst[5])
# print(mixed_lst[7])
# print(mixed_lst[8])

# print(mixed_lst[2:6])
# print(mixed_lst[2:6:2])
# print(mixed_lst[::-1])
# print(mixed_lst[-1])

# print(type(mixed_lst[2:6]))

# mixed_lst = [1, "Otar", 3.14, True, False, None, [1, [2], 3], "Hello World"]

# print(id(mixed_lst[0]))
# print(id(mixed_lst[6][0]))

# print(mixed_lst[6][3])
# print(mixed_lst[6][1][0])

# print(id(mixed_lst))

# a = 5
# b = 5

# print(id(a))
# print(id(b))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
#
# print(id(lst1))
# print(id(lst2))

# a = 1
# mixed_lst = [1, "Otar", 3.14, True, False, None, [1, 2, 3], "Hello World"]

# print(id(mixed_lst[0]))
# print(id(mixed_lst[6][0]))
# print(id(a))

# name = "Otar"
# name2 = "Otar"
#
# print(id(name))
# print(id(name2))

# mixed_lst = [1, "Otar", 3.14, True, False, None, [1, 2, 3], "Hello World"]
# copied = mixed_lst.copy()
# my_list = mixed_lst

# print(id(mixed_lst))
# print(id(copied))
# print(id(my_list))

# print(mixed_lst is copied)
# print(mixed_lst is my_list)

# print(mixed_lst == copied)
# print(mixed_lst == my_list)

# mixed_lst.append(25)
# mixed_lst.clear()

# print(mixed_lst)
# print(copied)
# print(my_list)

# mixed_lst.append(10)
# mixed_lst.append(" ")
# mixed_lst.append(5.55)
# mixed_lst.append("Tumanishvili")

# mixed_lst.clear()


# mixed_lst = [1, "Otar", 3.14, True, 1, False, True, None, [1, 2, 3], "Hello World", "Otar"]

# print(mixed_lst.count("Otar"))
# print(mixed_lst.count(1))

# for elem in mixed_lst:
#     print(elem)

# counter = 0
#
# for elem in mixed_lst:
#     if elem == 1 and type(elem) == int:
#         counter += 1
#
# print(counter)


# mixed_lst = [1, "Otar", 3.14, True, 1, False, True, None, [1, 2, 3], "Hello World", "Otar"]

# nums_list = [5, 8, 7, 6, 14, 2]

# nums_list.sort(reverse=True)

# print(nums_list)

# mixed_lst.remove(1)
# mixed_lst.remove(1)

# print(mixed_lst)

# mixed_lst.pop(2)

# mixed_lst.pop()
# mixed_lst.pop()
#
# popped_elem = mixed_lst.pop()
#
# print(popped_elem)
#
# print(mixed_lst)

# mixed_lst.insert(2, 8)

# lst = [5, 6, 7]

# mixed_lst.extend([2, 3])
# mixed_lst.append([2, 3])

# print(mixed_lst + lst)

# print(mixed_lst.index("Otar"))


# names = ["Otar", "Nino", "Alex", "John", 'ana']
#
# names.sort()
#
# print(names)


# mixed_lst = [1, "Otar", 3.14, True, 1, False, True, None, [1, 2, 3], "Hello World"]

# for i in range(len(mixed_lst)):
#     print(f"{i} -> {mixed_lst[i]}")

# for a, b in enumerate(mixed_lst):
#     print(f"{a} -> {b}")


# mixed_lst.reverse()
#
# print(mixed_lst)

# a, b = 5, 10
#
# print(a)
# print(b)

# a, *b, c = 5, 6
#
# print(a)
# print(b)
# print(c)


# lst = []
#
# for i in range(1, 31):
#     lst.append(i)
#
# print(lst)

# lst = [i * i for i in range(1, 31)]
#
# print(lst)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
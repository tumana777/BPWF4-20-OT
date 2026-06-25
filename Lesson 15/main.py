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
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def get_email(self, domain):
#         return f"{self.first_name}.{self.last_name}@{domain}"

    # def __repr__(self):
    #     return f"Student('{self.first_name}', '{self.last_name}', {self.age})"

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} is {self.age} years old"

# student = Student("Otar", "Tumanishvili", 35)
# student2 = Student("Nino", "Aleqsidze", 25)

# Student.__init__(student2, "Nino", "Aleqsidze", 25)

# print(student.get_full_name())
# print(student2.get_full_name())

# print(student.get_email("gmail.com"))
# print(student2.get_email("yahoo.com"))

# print(student)
# print(student2)


# class Student:
#     course = "Python"
#     pay = 1000
#     discount = 0.9
#     total_students = 0
#
#     def __init__(self, first_name, last_name, pay, discount):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.discount = discount
#         Student.total_students += 1
#
#     @classmethod
#     def get_discount(cls):
#         return cls.pay * cls.discount
#
#     @staticmethod
#     def get_rest():
#         day = input("Enter the day of the week: ")
#
#         if day == "sunday":
#             return "You can rest today"
#
#         return "You can't rest today"

# st1 = Student("Otar", "Tumanishvili", 1500, 0.8)
# st2 = Student("Nino", "Aleqsidze", 2000, 0.7)

# print(st1.get_discount())
# print(st2.get_discount())

# print(st1.get_rest())


# print(Student.total_students)

# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#         print("B")
#
# class C:
#     def show(self):
#         print("C")
#
# class D(A, C):
#     pass
#
# b = B()
# c = C()
# d = D()

# b.show()
# c.show()
# d.show()
# print(D.__mro__)

# class Vehicle:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def start(self):
#         return f"The {self.model} is now started"
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"The {self.model}'s speed is now {self.speed} km/h"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"The {self.model}'s speed is now {self.speed} km/h"
#
#     def brake(self):
#         self.speed = 0
#         return f"The {self.model} is stopped"
#
#     def __str__(self):
#         return f"{self.make} - {self.model}"
#
# class SUV(Vehicle):
#     def __init__(self, make, model, year, clearance):
#         super().__init__(make, model, year)
#         self.clearance = clearance
#
#     def off_road(self):
#         return f"The {self.model} can offroading."
#
#     def info(self):
#         return f"The {self.model}'s clearance is {self.clearance}"
#
# class Motorcycle(Vehicle):
#     def wheelie(self):
#         return f"The {self.model} can wheelie."
#
# toyota = SUV("Toyota", "Highlander", 2018, 250)
# honda = Motorcycle("Honda", "CBR", 2019)
#
# print(toyota.info())

# print(toyota.start())

# print(type(toyota))
# print(type(honda))

# print(toyota.start())
# print(toyota.accelerate(10))
# print(toyota.accelerate(10))
# print(toyota.accelerate(10))
# print(toyota.slow_down(5))
# print(toyota.brake())
# print(toyota.off_road())


# print(honda.start())
# print(honda.accelerate(10))
# print(honda.accelerate(10))
# print(honda.accelerate(10))
# print(honda.slow_down(5))
# print(honda.brake())
# print(honda.wheelie())


# class Vehicle:
#
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0
#
#     def start(self):
#         return f"The {self.model} is now started"
#
#     def accelerate(self, s):
#         self.speed += s
#         return f"The {self.model}'s speed is now {self.speed} km/h"
#
#     def slow_down(self, s):
#         self.speed -= s
#         return f"The {self.model}'s speed is now {self.speed} km/h"
#
#     def brake(self):
#         self.speed = 0
#         return f"The {self.model} is stopped"
#
#     def __str__(self):
#         return f"{self.make} - {self.model}"
#
# class ElectricVehicle:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity
#         self.battery_level = 100
#
#     def charge(self, amount):
#         self.battery_level = min(100, self.battery_level + amount)
#         return f"The battery level is now {self.battery_level}%"
#
#     def discharge(self, amount):
#         self.battery_level = max(0, self.battery_level - amount)
#         return f"The battery level is now {self.battery_level}%"
#
# class ElectricSUV(Vehicle, ElectricVehicle):
#     def __init__(self, make, model, year, battery_capacity):
#         Vehicle.__init__(self, make, model, year)
#         ElectricVehicle.__init__(self, battery_capacity)
#
#     def info(self):
#         return f"The {self.model}'s battery capacity is {self.battery_capacity} kWh"
#
# tesla = ElectricSUV("Tesla", "Model X", 2020, 90)
#
# print(tesla.discharge(10))
# print(tesla.info())
# print(tesla.charge(15))
# print(tesla.discharge(70))
# print(tesla.discharge(70))


# from abc import ABC, abstractmethod
#
# class Payment(ABC):
#     def __init__(self, amount):
#         self.__amount = amount
#
#     @property
#     def amount(self):
#         return self.__amount
#
#     def test(self):
#         return "test"
#
#     @abstractmethod
#     def pay(self):
#         pass
#
# class CashPayment(Payment):
#     def pay(self):
#         return f"Paid ${self.amount} with cash."
#
# class CreditCardPayment(Payment):
#     def pay(self):
#         return f"Paid ${self.amount} with credit card."
#
#
#
# cash = CashPayment(100)
# print(cash.pay())
#
# credit_card = CreditCardPayment(200)
# print(credit_card.pay())

























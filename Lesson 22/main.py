# Single Responsibility Principle
# Bad Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report for {self.data}"
#
#     def write_to_file(self, filename):
#         with open(filename, "w") as file:
#             file.write(self.generate_report())
#
# p = Report("Python")
# p.write_to_file("report.txt")

# Good Example

# class Report:
#     def __init__(self, data):
#         self.data = data
#
#     def generate_report(self):
#         return f"Report for {self.data}"
#
# class ReportWriter:
#     @staticmethod
#     def write_to_file(report: Report, filename):
#         with open(filename, "w") as file:
#             file.write(report.generate_report())
#
# r = Report("Python")
# rw = ReportWriter()
# rw.write_to_file(r, "report.txt")

# Open/Closed Principle
# Bad Example

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def apply_discount(self, discount_type):
#         if discount_type == "VIP":
#             return self.price * 0.9
#         elif discount_type == "Gold":
#             return self.price * 0.8
#         elif discount_type == "Silver":
#             return self.price * 0.7
#         else:
#             return self.price
#
# discount = Discount(100)
# print(discount.apply_discount("Gold"))

# Good Example

# from abc import ABC, abstractmethod
#
# class Discount(ABC):
#     def __init__(self, price):
#         self.price = price
#
#     @abstractmethod
#     def apply_discount(self):
#         pass
#
# class VIPDiscount(Discount):
#     def apply_discount(self):
#         return self.price * 0.9
#
# class GoldDiscount(Discount):
#     def apply_discount(self):
#         return self.price * 0.8
#
# class SilverDiscount(Discount):
#     def apply_discount(self):
#         return self.price * 0.7
#
# vip_discount = VIPDiscount(100)
# print(vip_discount.apply_discount())

# Liskov Substitution Principle
# Bad Example

# class Bird:
#     @staticmethod
#     def fly():
#         print("I can fly")
#
#     @staticmethod
#     def walk():
#         print("I can walk")
#
# class Sparrow(Bird):
#     @staticmethod
#     def fly():
#         print("I am a sparrow and I can fly")
#
#     @staticmethod
#     def walk():
#         print("I am a sparrow and I can walk")
#
# class Penguin(Bird):
#     @staticmethod
#     def walk():
#         print("I am a penguin and I can walk")
#
#     @staticmethod
#     def fly():
#         raise Exception("Penguins cannot fly")

# Good Example

# class Bird:
#     @staticmethod
#     def eat():
#         print("I can eat")
#
#     @staticmethod
#     def walk():
#         print("I can walk")
#
# class FlyingBird(Bird):
#     @staticmethod
#     def fly():
#         print("I can fly")
#
# class SwimmingBird(Bird):
#     @staticmethod
#     def swim():
#         print("I can swim")
#
# class Sparrow(FlyingBird):
#     pass
#
# class Penguin(SwimmingBird):
#     pass


# Interface Segregation Principle
# Bad Example

# class Worker:
#     @staticmethod
#     def work():
#         print("I am working")
#
#     @staticmethod
#     def eat():
#         print("I am eating")
#
# class Manager(Worker):
#     @staticmethod
#     def manage():
#         print("I am managing")
#
# manager = Manager()
#
# class Robot(Worker):
#     @staticmethod
#     def program():
#         print("I am programming")
#
#     @staticmethod
#     def charge():
#         print("I can charge my batteries")
#
# robot = Robot()


# Good Example
# from abc import ABC, abstractmethod
#
# class Workable(ABC):
#     @abstractmethod
#     def work(self):
#         pass
#
# class Eatable(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Chargeable(ABC):
#     @abstractmethod
#     def charge(self):
#         pass
#
# class Manager(Workable, Eatable):
#     def work(self):
#         print("I am working")
#
#     def eat(self):
#         print("I am eating")
#
# class Robot(Workable, Chargeable):
#     def work(self):
#         print("I am working")
#
#     def charge(self):
#         print("I can charge my batteries")
#
# r = Robot()
# m = Manager()
#
# r.work()
# r.charge()
#
# m.work()
# m.eat()

# Dependency Inversion Principle
# Bad Example

# class MySQLDatabase:
#     @staticmethod
#     def connect():
#         return "Connecting to MySQL database..."
#
# class Application:
#     def __init__(self):
#         self.db = MySQLDatabase()
#
#     def run(self):
#         return self.db.connect()
#
# app = Application()
#
# print(app.run())

# Good Example

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL database..."

class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connecting to PostgreSQL database..."

class SQLiteDatabase(Database):
    def connect(self):
        return "Connecting to SQLite database..."

class Application:
    def __init__(self, db: Database):
        self.db = db

    def run(self):
        return self.db.connect()

mysql_app = Application(MySQLDatabase())
print(mysql_app.run())

postgresql_app = Application(PostgreSQLDatabase())
print(postgresql_app.run())

sqlite_app = Application(SQLiteDatabase())
print(sqlite_app.run())
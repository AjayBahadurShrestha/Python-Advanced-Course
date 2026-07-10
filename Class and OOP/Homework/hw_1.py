#1. Create a Simple Class (Easy)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Subodh", 18)

print("Student Information")
print("Name:", student1.name)
print("Age:", student1.age)


#2. Using a Constructor 
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)

emp = Employee(101, "Ram", 50000)
emp.display()

#3. Class with Methods 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())



#4. Student Grade System 
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        per = self.percentage()

        if per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

marks = [80, 75, 90, 70, 85]

s = Student("Subodh", 1, marks)
s.display()

#5. Bank Account System (Medium)
class BankAccount:
    def __init__(self, acc_no, holder, balance):
        self.acc_no = acc_no
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:", self.balance)

acc = BankAccount(1001, "Subodh", 5000)

acc.deposit(2000)
acc.withdraw(3000)
acc.withdraw(10000)
acc.display_balance()


#6. Library Management (Medium)
class Book:
    def __init__(self, book_id, name, author, price):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Book Name:", self.name)
        print("Author:", self.author)
        print("Price:", self.price)

    def update_price(self, new_price):
        self.price = new_price

    def discount(self):
        self.price = self.price * 0.9

book = Book(1, "Python", "ABC", 1000)

book.display()
book.update_price(1200)
book.discount()

print("\nAfter Update and Discount")
book.display()
#7. Car Showroom Management (Medium-Hard)
class Car:
    def __init__(self, brand, model, price, fuel):
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = fuel

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel:", self.fuel)

    def affordable(self):
        if self.price < 3000000:
            print("Affordable Car")
        else:
            print("Not Affordable")

    def discount(self, percent):
        self.price -= self.price * percent / 100

car = Car("Toyota", "Yaris", 2800000, "Petrol")

car.display()
car.affordable()

d = float(input("Enter discount percentage: "))
car.discount(d)

print("\nAfter Discount")
car.display()
#8. Multiple Objects (Hard)
class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        print(self.pid, self.name, self.price)

products = [
    Product(1, "Laptop", 90000),
    Product(2, "Phone", 35000),
    Product(3, "Mouse", 1200),
    Product(4, "Keyboard", 2500),
    Product(5, "Monitor", 18000)
]

print("All Products")
for p in products:
    p.display()

expensive = max(products, key=lambda x: x.price)
cheap = min(products, key=lambda x: x.price)

average = sum(p.price for p in products) / len(products)

print("\nMost Expensive:")
expensive.display()

print("\nCheapest:")
cheap.display()

print("\nAverage Price:", average)
#9. School Management System (Hard)
class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience

    def display(self):
        print(self.name, self.subject, self.experience)

    def senior(self):
        if self.experience >= 10:
            print("Senior Teacher")
        else:
            print("Junior Teacher")

    def promotion(self):
        self.experience += 1

teachers = [
    Teacher("Ram", "Math", 12),
    Teacher("Sita", "Science", 8),
    Teacher("Hari", "English", 15)
]

for t in teachers:
    t.display()
    t.senior()
    t.promotion()
    print("After Promotion:", t.experience)
    print()
#10. Inventory Management System (Advanced)
class Inventory:
    def __init__(self, pid, name, quantity, price):
        self.pid = pid
        self.name = name
        self.quantity = quantity
        self.price = price

    def add_stock(self, qty):
        self.quantity += qty

    def remove_stock(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
        else:
            print("Not enough stock.")

    def total_value(self):
        return self.quantity * self.price

    def low_stock(self):
        if self.quantity < 10:
            return "Low Stock"
        return "Stock OK"

    def display(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Inventory Value:", self.total_value())
        print("Status:", self.low_stock())
        print()

items = [
    Inventory(1, "Laptop", 5, 90000),
    Inventory(2, "Mouse", 30, 1200),
    Inventory(3, "Keyboard", 8, 2500)
]

items[0].add_stock(5)
items[1].remove_stock(10)

print("Inventory Report\n")

for item in items:
    item.display()
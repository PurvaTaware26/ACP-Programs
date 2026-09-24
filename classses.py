#1. Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")

student1 = Student(1, "Rahul", [80, 75, 90, 85, 70])
student2 = Student(2, "Sneha", [85, 90, 88, 92, 80])
student3 = Student(3, "Amit", [70, 65, 75, 80, 72])

student1.display()
student2.display()
student3.display()


#2. Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def calculate_gross_salary(self):
        hra = self.calculate_hra()
        da = self.calculate_da()
        return self.basic_salary + hra + da

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.calculate_gross_salary())

employee1 = Employee(101, "Rahul", 30000)
employee2 = Employee(102, "Sneha", 40000)

employee1.display()
print("--------------------")
employee2.display()


#3. Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())

rectangle1 = Rectangle(10, 5)
rectangle1.display()



#4. Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Circumference:", self.circumference())

circle1 = Circle(7)
circle1.display()

#5. Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book1 = Book(101, "Python Basics", "John", 450)
book2 = Book(102, "Data Science", "Smith", 550)
book3 = Book(103, "Machine Learning", "David", 600)

book1.display()

book2.display()

book3.display()


#6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.

class ElectricityBill:
    def __init__(self, number, name, units):
        self.number = number
        self.name = name
        self.units = units

    def bill(self):
        if self.units <= 100:
            amount = self.units * 5
        elif self.units <= 200:
            amount = (100 * 5) + (self.units - 100) * 7
        else:
            amount = (100 * 5) + (100 * 7) + (self.units - 200) * 10
        return amount

    def display(self):
        print("Consumer Number:", self.number)
        print("Consumer Name:", self.name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.bill())

consumer1 = ElectricityBill(101, "Rahul", 250)
consumer1.display()

#7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discount(self):
        discount = self.price * 0.10
        return self.price - discount

    def show(self):
        self.display()
        print("Price after discount:", self.discount())

phone1 = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)
phone1.show()


#8. Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def bill(self):
        medicine = 1000
        return self.fee + medicine

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.fee)
        print("Total Bill:", self.bill())

patient1 = Patient(101, "Rahul", 25, "Fever", 500)
patient1.display()


#9. Design an ATM class that allows a user to check balance, deposit money, withdraw money, and display account details. Create an object of the class and implement the operations through a menu-driven program.

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)

account1 = ATM(1001, "Rahul", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account1.check()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        account1.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        account1.withdraw(amount)
    elif choice == 4:
        account1.display()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")


#10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.

class Vehicle:
    def __init__(self, number, model, rate):
        self.number = number
        self.model = model
        self.rate = rate
        self.available = True

    def rent(self, days):
        if self.available:
            self.available = False
            charge = self.rate * days
            print("Vehicle Rented")
            print("Rental Charges:", charge)
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle Returned")

    def display(self):
        print("Vehicle Number:", self.number)
        print("Model:", self.model)
        print("Rental Rate:", self.rate)
        print("Available:", self.available)

vehicle1 = Vehicle("MH12AB1234", "Swift", 1000)

vehicle1.display()
vehicle1.rent(3)
vehicle1.return_vehicle()
vehicle1.display()


#11. Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.

class ShoppingCart:
    def __init__(self, name, cart_id):
        self.name = name
        self.cart_id = cart_id
        self.products = []

    def add(self, product, price):
        self.products.append([product, price])
        print(product, "added")

    def remove(self, product):
        for item in self.products:
            if item[0] == product:
                self.products.remove(item)
                print(product, "removed")
                return
        print("Product not found")

    def total(self):
        amount = 0
        for item in self.products:
            amount = amount + item[1]
        return amount

    def display(self):
        print("Customer Name:", self.name)
        print("Cart ID:", self.cart_id)
        print("Total Bill:", self.total())

    def __del__(self):
        print("Shopping Cart Destroyed")

cart1 = ShoppingCart("Rahul", 101)

cart1.add("Shirt", 800)
cart1.add("Shoes", 1500)
cart1.add("Watch", 1000)

cart1.remove("Watch")
cart1.display()


#12. Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.


class FoodOrder:
    def __init__(self, order_id, name, food, quantity, price):
        self.order_id = order_id
        self.name = name
        self.food = food
        self.quantity = quantity
        self.price = price

    def bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.name)
        print("Food Item:", self.food)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.bill())

    def __del__(self):
        print("Order Completed")

order1 = FoodOrder(101, "Sneha", "Pizza", 2, 300)
order1.display()


#13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return (self.total() / 500) * 100

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student Result Completed")

student1 = StudentResult("Rahul", [80, 75, 90, 85, 70])
student1.display()


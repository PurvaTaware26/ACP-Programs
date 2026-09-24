#1. Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes and override the area() method in each class. Create objects of each class and demonstrate runtime polymorphism.
class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle1 = Circle(7)
rectangle1 = Rectangle(10, 5)
triangle1 = Triangle(10, 6)

print("Circle Area:", circle1.area())
print("Rectangle Area:", rectangle1.area())
print("Triangle Area:", triangle1.area())


#2. Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and Tester classes. Override the method in each class to calculate salary according to the employee's role.

class Employee:
    def calculate_salary(self):
        return 0


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 50000 * 0.30


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 40000 * 0.20


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 35000 * 0.15


manager1 = Manager()
developer1 = Developer()
tester1 = Tester()

print("Manager Salary:", manager1.calculate_salary())
print("Developer Salary:", developer1.calculate_salary())
print("Tester Salary:", tester1.calculate_salary())


#3. Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle.

class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self start")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine")


car1 = Car()
bike1 = Bike()
bus1 = Bus()

car1.start()
bike1.start()
bus1.start()


#4. Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion. Override sound() in each class to display the appropriate sound.

class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says: Roar")


dog1 = Dog()
cat1 = Cat()
cow1 = Cow()
lion1 = Lion()

dog1.sound()
cat1.sound()
cow1.sound()
lion1.sound()


#5. Create a base class Notification with a method send(). Derive EmailNotification, SMSNotification, and PushNotification. Override send() to display the appropriate notification method.

class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


email1 = EmailNotification()
sms1 = SMSNotification()
push1 = PushNotification()

email1.send()
sms1.send()
push1.send()


#6. Create a base class Student with a method calculate_grade(). Derive EngineeringStudent, MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.


class Student:
    def calculate_grade(self, marks):
        return "Grade"


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "D"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 55:
            return "C"
        else:
            return "D"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "D"


engineering1 = EngineeringStudent()
medical1 = MedicalStudent()
management1 = ManagementStudent()

print("Engineering Grade:", engineering1.calculate_grade(85))
print("Medical Grade:", medical1.calculate_grade(78))
print("Management Grade:", management1.calculate_grade(70))


#7. Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount, CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently for each account type.

class BankAccount:
    def calculate_interest(self, balance):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


savings1 = SavingsAccount()
current1 = CurrentAccount()
fixed1 = FixedDepositAccount()

print("Savings Interest:", savings1.calculate_interest(50000))
print("Current Interest:", current1.calculate_interest(50000))
print("Fixed Deposit Interest:", fixed1.calculate_interest(50000))


#8. Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and HTMLReport. Override generate() in each class. Write a function that accepts any report object and calls generate().


class Report:
    def generate(self):
        print("Generating report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def show(report):
    report.generate()


pdf1 = PDFReport()
excel1 = ExcelReport()
html1 = HTMLReport()

show(pdf1)
show(excel1)
show(html1)


#9. Create a class Distance with feet and inches. Overload the + operator to add two distance objects and display the result in normalized form.


class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        feet = self.feet + other.feet
        inches = self.inches + other.inches

        feet = feet + inches // 12
        inches = inches % 12

        return Distance(feet, inches)

    def display(self):
        print("Distance:", self.feet, "feet", self.inches, "inches")


distance1 = Distance(5, 8)
distance2 = Distance(3, 7)

distance3 = distance1 + distance2
distance3.display()


#10. Create a class Student containing the student's name and total marks. Overload the > and < operators to compare the marks of two students.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student("Rahul", 450)
student2 = Student("Sneha", 420)

print("Student 1 has greater marks:", student1 > student2)
print("Student 1 has smaller marks:", student1 < student2)


#11. Create a class Product with product name and price. Overload the == and > operators to compare two products based on their prices.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 60000)

print("Prices are equal:", product1 == product2)
print("Product 1 is costlier:", product1 > product2)


#12. Develop an online shopping payment module using polymorphism. Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement its own make_payment() method. Demonstrate polymorphism using a common function.


class Payment:
    def make_payment(self):
        print("Making payment")


class UPIPayment(Payment):
    def make_payment(self):
        print("Payment made using UPI")


class CardPayment(Payment):
    def make_payment(self):
        print("Payment made using Card")


class WalletPayment(Payment):
    def make_payment(self):
        print("Payment made using Wallet")


def pay(payment):
    payment.make_payment()


upi1 = UPIPayment()
card1 = CardPayment()
wallet1 = WalletPayment()

pay(upi1)
pay(card1)
pay(wallet1)


#13. Create a base class Person with a method display_role(). Derive Student, Faculty, and Administrator. Override the method to display the respective role. Store all objects in a list and invoke the same method using a loop.

class Person:
    def display_role(self):
        print("Person")


class Student(Person):
    def display_role(self):
        print("Student")


class Faculty(Person):
    def display_role(self):
        print("Faculty")


class Administrator(Person):
    def display_role(self):
        print("Administrator")


people = [Student(), Faculty(), Administrator()]

for person in people:
    person.display_role()


#14. Create a base class Media with a method play(). Derive Audio, Video, and Podcast. Override play() according to the media type.

class Media:
    def play(self):
        print("Playing media")


class Audio(Media):
    def play(self):
        print("Playing audio")


class Video(Media):
    def play(self):
        print("Playing video")


class Podcast(Media):
    def play(self):
        print("Playing podcast")


audio1 = Audio()
video1 = Video()
podcast1 = Podcast()

audio1.play()
video1.play()
podcast1.play()


#15. Create a base class SmartDevice with methods turn_on() and turn_off(). Derive Light, Fan, AC, and TV. Override the methods according to each device.

class SmartDevice:
    def turn_on(self):
        print("Device is ON")

    def turn_off(self):
        print("Device is OFF")


class Light(SmartDevice):
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is ON")

    def turn_off(self):
        print("Fan is OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is ON")

    def turn_off(self):
        print("TV is OFF")


light1 = Light()
fan1 = Fan()
ac1 = AC()
tv1 = TV()

light1.turn_on()
light1.turn_off()

fan1.turn_on()
fan1.turn_off()

ac1.turn_on()
ac1.turn_off()

tv1.turn_on()
tv1.turn_off()

#1. Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        super().display()
        print("Department:", self.department)
        print("Annual Salary:", self.annual_salary())

employee1 = Employee(101, "Rahul", 30000)
manager1 = Manager(102, "Sneha", 50000, "IT")
employee1.display()
manager1.display()


#2. Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discount(self):
        return self.price - (self.price * 0.10)

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)
        print("Discounted Price:", self.discount())
car1 = Car("Toyota", "Innova", "Petrol", 2000000)
car1.display()


#3. Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.
class Academic:
    def __init__(self, marks):
        self.marks = marks
    def academic(self):
        return sum(self.marks)
class Sports:
    def __init__(self, points):
        self.points = points
    def sports(self):
        return self.points
class Student(Academic, Sports):
    def __init__(self, name, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)
        self.name = name

    def performance(self):
        return self.academic() + self.sports()

    def display(self):
        print("Name:", self.name)
        print("Academic Marks:", self.academic())
        print("Sports Points:", self.sports())
        print("Overall Performance:", self.performance())


student1 = Student("Rahul", [80, 85, 90], 20)
student1.display()



#4. Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee1 = Employee("Rahul", 25, 101, "Developer", 50000)
employee1.display()


#5. Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)


student1 = ResearchStudent("Rahul", 22, 101, "CSE", "Artificial Intelligence", "Dr. Sharma")
student1.display()


#6. Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.

class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, rate):
        super().__init__(account_no, balance)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, rate, benefits):
        super().__init__(account_no, balance, rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.rate, "%")
        print("Interest:", self.interest())
        print("Benefits:", self.benefits)


account1 = PremiumSavingsAccount(1001, 50000, 6, "Free ATM and Insurance")
account1.display()


#7. Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.


class Shape:
    def display(self):
        print("Shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def display(self):
        print("Circle")
        print("Area:", self.area())


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        print("Rectangle")
        print("Area:", self.area())


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def display(self):
        print("Triangle")
        print("Area:", self.area())


circle1 = Circle(7)
rectangle1 = Rectangle(10, 5)
triangle1 = Triangle(10, 6)

circle1.display()
rectangle1.display()
triangle1.display()


#8. Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.


class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


class Manager(Employee):
    def salary1(self):
        return self.salary + self.salary * 0.30

    def display(self):
        print("Manager:", self.name)
        print("Salary:", self.salary1())


class Developer(Employee):
    def salary1(self):
        return self.salary + self.salary * 0.20

    def display(self):
        print("Developer:", self.name)
        print("Salary:", self.salary1())


class Tester(Employee):
    def salary1(self):
        return self.salary + self.salary * 0.15

    def display(self):
        print("Tester:", self.name)
        print("Salary:", self.salary1())


manager1 = Manager(101, "Rahul", 50000)
developer1 = Developer(102, "Sneha", 45000)
tester1 = Tester(103, "Amit", 40000)

manager1.display()
developer1.display()
tester1.display()


#9. Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


assistant1 = TeachingAssistant("Rahul", 22, 101, "Python")
assistant1.display()


#10. Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed)


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery)


car1 = SportsCar("BMW", "M4", "250 km/h")
bike1 = ElectricBike("Ola", "S1", "5 kWh")

car1.display()

bike1.display()


#11. Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.

class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        percentage = self.percentage()

        if percentage >= 80:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

student1 = Result(101, "Rahul", "CSE", [80, 85, 90])
student1.display()



#12. Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self):
        return self.price - (self.price * 0.10)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price())


product1 = ElectronicProduct(101, "Laptop", 60000, "HP", "2 Years")
product1.display()

#13. Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        self.print_document()
        self.scan_document()


device1 = MultifunctionDevice()
device1.display()

#14. Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.

class Camera:
    def photo(self):
        print("Taking photograph")


class Phone:
    def call(self):
        print("Making call")


class Smartphone(Camera, Phone):
    def display(self):
        self.photo()
        self.call()


phone1 = Smartphone()
phone1.display()

#15. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)


student1 = ResearchStudent("Rahul", 22, 101, "CSE", "Machine Learning", "Dr. Sharma")
student1.display()



#16. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)
student1 = ResearchStudent("Sneha", 23, 102, "CSE", "Artificial Intelligence", "Dr. Patil")
student1.display()



#17. Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.

class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")

    def behavior(self):
        print("Dog is friendly")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

    def behavior(self):
        print("Cat is playful")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")

    def behavior(self):
        print("Cow is calm")


dog1 = Dog("Tommy")
cat1 = Cat("Kitty")
cow1 = Cow("Gauri")

dog1.display()
dog1.sound()
dog1.behavior()


cat1.display()
cat1.sound()
cat1.behavior()

cow1.display()
cow1.sound()
cow1.behavior()




#18. Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)


class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, research):
        super().__init__(name, age, specialization)
        self.research = research

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)
        print("Research:", self.research)


surgeon1 = Surgeon("Rahul", 40, "Cardiology", "Heart Disease")
researcher1 = MedicalResearcher("Sneha", 35, "Neurology", "Brain Research")

surgeon1.display()
researcher1.display()
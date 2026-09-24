#1. Abstract Shape

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


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


#2. Abstract Vehicle

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


car1 = Car()
bike1 = Bike()
bus1 = Bus()

car1.start()
car1.stop()

bike1.start()
bike1.stop()

bus1.start()
bus1.stop()


#3. Abstract BankAccount

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount Withdrawn:", amount)


savings1 = SavingsAccount(10000)
current1 = CurrentAccount(20000)

savings1.deposit(5000)
savings1.withdraw(3000)
print("Savings Balance:", savings1.balance)

current1.deposit(5000)
current1.withdraw(8000)
print("Current Balance:", current1.balance)


#4. Abstract FoodOrder

from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, price):
        self.price = price

    def calculate_bill(self):
        return self.price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, price):
        self.price = price

    def calculate_bill(self):
        return self.price + self.delivery_charge()

    def delivery_charge(self):
        return 50


order1 = RestaurantOrder(500)
order2 = HomeDeliveryOrder(500)

print("Restaurant Bill:", order1.calculate_bill())
print("Restaurant Delivery Charge:", order1.delivery_charge())

print("Home Delivery Bill:", order2.calculate_bill())
print("Home Delivery Charge:", order2.delivery_charge())


#5. Abstract Patient


from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment with hospital stay")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient treatment")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency treatment")


patient1 = InPatient()
patient2 = OutPatient()
patient3 = EmergencyPatient()

print("In-Patient Bill:", patient1.calculate_bill())
patient1.treatment()

print("Out-Patient Bill:", patient2.calculate_bill())
patient2.treatment()

print("Emergency Patient Bill:", patient3.calculate_bill())
patient3.treatment()


#6. Abstract Transport

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 5


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10


bus1 = Bus()
train1 = Train()
taxi1 = Taxi()
flight1 = Flight()

distance = 100

print("Bus Fare:", bus1.calculate_fare(distance))
print("Train Fare:", train1.calculate_fare(distance))
print("Taxi Fare:", taxi1.calculate_fare(distance))
print("Flight Fare:", flight1.calculate_fare(distance))


#7. Abstract Question

from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct):
        self.correct = correct

    def evaluate_answer(self, answer):
        if answer == self.correct:
            return "Correct Answer"
        else:
            return "Wrong Answer"


class TrueFalseQuestion(Question):
    def __init__(self, correct):
        self.correct = correct

    def evaluate_answer(self, answer):
        if answer == self.correct:
            return "Correct Answer"
        else:
            return "Wrong Answer"


class DescriptiveQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.answer.lower():
            return "Correct Answer"
        else:
            return "Answer Submitted"


mcq1 = MCQQuestion("B")
tf1 = TrueFalseQuestion("True")
descriptive1 = DescriptiveQuestion("Python")

print("MCQ:", mcq1.evaluate_answer("B"))
print("True/False:", tf1.evaluate_answer("True"))
print("Descriptive:", descriptive1.evaluate_answer("Python"))


#8. Abstract Authentication


from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


password1 = PasswordAuthentication()
otp1 = OTPAuthentication()
biometric1 = BiometricAuthentication()

password1.authenticate()
otp1.authenticate()
biometric1.authenticate()


#9. Abstract CloudStorage

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


drive1 = GoogleDrive()
dropbox1 = Dropbox()
onedrive1 = OneDrive()

drive1.upload_file()
drive1.download_file()
drive1.delete_file()

dropbox1.upload_file()
dropbox1.download_file()
dropbox1.delete_file()

onedrive1.upload_file()
onedrive1.download_file()
onedrive1.delete_file()


#10. Abstract Appointment

from abc import ABC, abstractmethod

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


general1 = GeneralAppointment()
specialist1 = SpecialistAppointment()
emergency1 = EmergencyAppointment()

general1.book_appointment()
print("Fee:", general1.calculate_fee())

specialist1.book_appointment()
print("Fee:", specialist1.calculate_fee())

emergency1.book_appointment()
print("Fee:", emergency1.calculate_fee())


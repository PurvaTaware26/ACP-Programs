print("Question 1:")

# 1. Write a function factorial(n) that accepts an integer and returns its factorial.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
n1 = int(input("Enter a number: "))
print("Factorial:", factorial(n1))


print("\nQuestion 2:")

# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
n2 = int(input("Enter a number: "))
print("Number is:", check_even_odd(n2))


print("\nQuestion 3:")

# 3. Define a function that accepts two numbers and returns the greater number.
def greater_number(a, b):
    if a > b:
        return a
    else:
        return b
a3 = int(input("Enter first number: "))
b3 = int(input("Enter second number: "))
print("Greater number:", greater_number(a3, b3))


print("\nQuestion 4:")
# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si
p4 = float(input("Enter principal: "))
r4 = float(input("Enter rate: "))
t4 = float(input("Enter time: "))
print("Simple Interest:", simple_interest(p4, r4, t4))


print("\nQuestion 5:")
# 5. Write a function is_prime(n) that returns True if a number is prime otherwise False.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n5 = int(input("Enter a number: "))
if is_prime(n5):
    print("Prime number")
else:
    print("Not a prime number")


print("\nQuestion 6:")
# 6. Define a function to calculate the area of a circle using its radius.
def circle_area(radius):
    area = 3.14 * radius * radius
    return area
radius6 = float(input("Enter radius: "))
print("Area of circle:", circle_area(radius6))


print("\nQuestion 7:")
# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n7 = int(input("Enter n: "))
print("Sum:", natural_sum(n7))


print("\nQuestion 8:")
# 8. Create a function power(base, exponent) to calculate base raised to exponent.
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result
base8 = int(input("Enter base: "))
exponent8 = int(input("Enter exponent: "))
print("Answer:", power(base8, exponent8))


print("\nQuestion 9:")
# 9. Write a function that accepts a list of numbers and returns the largest element without using max().
def largest_element(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest
numbers9 = list(map(int, input("Enter numbers: ").split()))
print("Largest element:", largest_element(numbers9))


print("\nQuestion 10:")
# 10. Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count
text10 = input("Enter a string: ")
print("Number of vowels:", count_vowels(text10))


print("\nQuestion 11:")
# 11. Write a function that accepts a string and returns its reverse.
def reverse_string(text):
    return text[::-1]
text11 = input("Enter a string: ")
print("Reverse:", reverse_string(text11))


print("\nQuestion 12:")

# 12. Create a function that checks whethera given string or number is a palindrome.
def is_palindrome(value):
    value = str(value)
    if value == value[::-1]:
        return True
    else:
        return False
value12 = input("Enter a string or number: ")
if is_palindrome(value12):
    print("Palindrome")
else:
    print("Not a palindrome")


print("\nQuestion 13:")
# 13. Write a function that accepts a list of numbers and returns their average.

def average(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)
numbers13 = list(map(int, input("Enter numbers: ").split()))
print("Average:", average(numbers13))


print("\nQuestion 14:")
# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occurrences(numbers, element):
    count = 0
    for i in numbers:
        if i == element:
            count = count + 1
    return count
numbers14 = list(map(int, input("Enter numbers: ").split()))
element14 = int(input("Enter element: "))
print("Number of occurrences:", count_occurrences(numbers14, element14))


print("\nQuestion 15:")
# 15. Write a function that accepts a list and returns a new list containing only unique elements.

def unique_elements(numbers):
    result = []
    for i in numbers:
        if i not in result:
            result.append(i)
    return result
numbers15 = list(map(int, input("Enter numbers: ").split()))
print("Unique elements:", unique_elements(numbers15))


print("\nQuestion 16:")
# 16. Create a function to find the second-largest number in a list.
def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]
    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    return second
numbers16 = list(map(int, input("Enter numbers: ").split()))
print("Second largest:", second_largest(numbers16))


print("\nQuestion 17:")
# 17. Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        a = b
        b = a + b
    return result
n17 = int(input("Enter n: "))
print("Fibonacci numbers:", fibonacci(n17))


print("\nQuestion 18:")
# 18. Create a function that accepts marks in five subjects and returns percentage and grade.

def calculate_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

percentage18, grade18 = calculate_result(m1, m2, m3, m4, m5)

print("Percentage:", percentage18)
print("Grade:", grade18)


print("\nQuestion 19:")

# 19. Write a function that accepts the number of units
# consumed and calculates the electricity bill.

def electricity_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    return bill

units19 = float(input("Enter units consumed: "))

print("Electricity Bill:", electricity_bill(units19))


print("\nQuestion 20:")

# 20. Write a function that accepts basic salary
# and calculates gross salary after adding HRA and DA.

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10

    gross = basic + hra + da

    return gross

basic20 = float(input("Enter basic salary: "))

print("Gross Salary:", gross_salary(basic20))


print("\nQuestion 21:")

# 21. Create a function that accepts item prices and quantities
# and returns total bill after applying discount.

def total_bill(prices, quantities, discount):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount_amount = total * discount / 100
    final_bill = total - discount_amount

    return final_bill

prices21 = list(map(float, input("Enter prices: ").split()))
quantities21 = list(map(int, input("Enter quantities: ").split()))
discount21 = float(input("Enter discount percentage: "))

print("Final Bill:", total_bill(prices21, quantities21, discount21))


print("\nQuestion 22:")

# 22. Write a function that accepts a list of numbers
# and returns minimum, maximum, sum and average.

def calculate_values(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0

    for i in numbers:
        if i < minimum:
            minimum = i

        if i > maximum:
            maximum = i

        total = total + i

    average = total / len(numbers)

    return minimum, maximum, total, average

numbers22 = list(map(int, input("Enter numbers: ").split()))

minimum22, maximum22, sum22, average22 = calculate_values(numbers22)

print("Minimum:", minimum22)
print("Maximum:", maximum22)
print("Sum:", sum22)
print("Average:", average22)


print("\nQuestion 23:")

# 23. Write a program using separate functions to process
# student records containing name, roll number and marks.

def student_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


students = []

n23 = int(input("Enter number of students: "))

for i in range(n23):
    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = list(map(int, input("Enter 5 marks: ").split()))

    total, percentage, grade = student_result(marks)

    student = {
        "Name": name,
        "Roll Number": roll,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)

class_total = 0

for student in students:
    class_total = class_total + student["Percentage"]

class_average = class_total / n23

highest = students[0]
lowest = students[0]

for student in students:
    if student["Percentage"] > highest["Percentage"]:
        highest = student

    if student["Percentage"] < lowest["Percentage"]:
        lowest = student

print("\nStudent Records:")

for student in students:
    print(student)

print("Class Average:", class_average)
print("Highest Scorer:", highest["Name"])
print("Lowest Scorer:", lowest["Name"])


print("\nQuestion 24:")

# 24. Create functions for deposit, withdrawal,
# balance enquiry and transaction history.

balance = 0
transactions = []


def deposit(amount):
    global balance

    balance = balance + amount
    transactions.append("Deposited " + str(amount))


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")


def balance_enquiry():
    print("Balance:", balance)


def transaction_history():
    print("Transaction History:")

    for transaction in transactions:
        print(transaction)


deposit(5000)
withdrawal(1000)
balance_enquiry()
transaction_history()


print("\nQuestion 25:")

# 25. Create functions to add books, issue books,
# return books, search books and display available books.

books = {
    "Python": True,
    "Java": True,
    "C++": True
}


def add_book(name):
    books[name] = True
    print("Book added")


def issue_book(name):
    if name in books and books[name] == True:
        books[name] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(name):
    if name in books:
        books[name] = True
        print("Book returned")


def search_book(name):
    if name in books:
        print("Book found")
    else:
        print("Book not found")


def display_books():
    print("Available Books:")

    for name in books:
        if books[name] == True:
            print(name)


add_book("Python Programming")
issue_book("Python")
return_book("Python")
search_book("Java")
display_books()


print("\nQuestion 26:")

# 26. Develop a modular program using functions to calculate
# electricity bills using different consumption slabs.
# Include fixed charges, taxes and discounts.

def slab_bill(units):
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    return bill


def fixed_charge():
    return 100


def tax(amount):
    return amount * 0.05


def discount(amount):
    if amount > 1000:
        return amount * 0.10
    else:
        return 0


units26 = float(input("Enter units consumed: "))

energy_charge = slab_bill(units26)
fixed = fixed_charge()

subtotal = energy_charge + fixed
tax_amount = tax(subtotal)
discount_amount = discount(subtotal)

final_bill = subtotal + tax_amount - discount_amount

print("Energy Charge:", energy_charge)
print("Fixed Charge:", fixed)
print("Tax:", tax_amount)
print("Discount:", discount_amount)
print("Final Bill:", final_bill)


print("\nQuestion 27:")

# 27. Create functions to calculate consultation charges,
# laboratory charges, medicine charges and room charges.

def consultation_charge():
    return 500


def laboratory_charge():
    return 1000


def medicine_charge():
    return 1500


def room_charge():
    return 2000


def patient_discount(category, amount):
    if category == "senior":
        return amount * 0.20
    elif category == "child":
        return amount * 0.10
    else:
        return 0


def final_hospital_bill(category):
    total = consultation_charge()
    total = total + laboratory_charge()
    total = total + medicine_charge()
    total = total + room_charge()

    discount = patient_discount(category, total)

    return total - discount


category27 = input("Enter patient category: ")

print("Final Bill:", final_hospital_bill(category27))


print("\nQuestion 28:")

# 28. Implement functions to add/remove products,
# calculate subtotal, apply coupon discounts,
# calculate GST and generate final invoice.

products28 = {}


def add_product(name, price):
    products28[name] = price


def remove_product(name):
    if name in products28:
        del products28[name]


def subtotal():
    total = 0

    for price in products28.values():
        total = total + price

    return total


def coupon_discount(amount):
    return amount * 0.10


def calculate_gst(amount):
    return amount * 0.18


def generate_invoice():
    sub = subtotal()
    discount = coupon_discount(sub)

    amount = sub - discount
    gst = calculate_gst(amount)

    final_amount = amount + gst

    print("Subtotal:", sub)
    print("Discount:", discount)
    print("GST:", gst)
    print("Final Amount:", final_amount)


add_product("Pen", 20)
add_product("Book", 100)
add_product("Bag", 500)

generate_invoice()


print("\nQuestion 29:")

# 29. Write a recursive function to search for an element
# in a sorted list using binary search.

def binary_search(numbers, low, high, element):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == element:
        return mid
    elif element < numbers[mid]:
        return binary_search(numbers, low, mid - 1, element)
    else:
        return binary_search(numbers, mid + 1, high, element)


numbers29 = list(map(int, input("Enter sorted numbers: ").split()))
element29 = int(input("Enter element to search: "))

position = binary_search(numbers29, 0, len(numbers29) - 1, element29)

if position == -1:
    print("Element not found")
else:
    print("Element found at index:", position)


print("\nQuestion 30:")

# 30. Convert a decimal number into binary using recursion
# without using Python built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


n30 = int(input("Enter decimal number: "))

if n30 == 0:
    print("Binary: 0")
else:
    print("Binary:", decimal_to_binary(n30))


print("\nQuestion 31:")

# 31. Check whether a string is a palindrome using recursion.

def palindrome(text, start, end):
    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return palindrome(text, start + 1, end - 1)


text31 = input("Enter a string: ")

if palindrome(text31, 0, len(text31) - 1):
    print("Palindrome")
else:
    print("Not a palindrome")


print("\nQuestion 32:")

# 32. Create separate functions for addition, subtraction,
# multiplication and division. Pass these functions as
# arguments to another function called calculate().

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(operation, a, b):
    return operation(a, b)


a32 = float(input("Enter first number: "))
b32 = float(input("Enter second number: "))

print("Addition:", calculate(addition, a32, b32))
print("Subtraction:", calculate(subtraction, a32, b32))
print("Multiplication:", calculate(multiplication, a32, b32))

if b32 != 0:
    print("Division:", calculate(division, a32, b32))
else:
    print("Division not possible")
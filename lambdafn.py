print("Question 1:")
# 1. Write a lambda function to calculate the square of a given number.
square = lambda n: n * n
n1 = int(input("Enter a number: "))
print("Square:", square(n1))


print("\nQuestion 2:")
# 2. Create a lambda function that returns the cube of a number.
cube = lambda n: n * n * n
n2 = int(input("Enter a number: "))
print("Cube:", cube(n2))


print("\nQuestion 3:")
# 3. Write a lambda function that returns True if a number is even and False otherwise.
even_odd = lambda n: n % 2 == 0
n3 = int(input("Enter a number: "))
print("Even:", even_odd(n3))


print("\nQuestion 4:")
# 4. Use a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
a4 = int(input("Enter first number: "))
b4 = int(input("Enter second number: "))
print("Maximum:", maximum(a4, b4))


print("\nQuestion 5:")
# 5. Create a lambda function to calculate simple interest using principal, rate and time.
simple_interest = lambda p, r, t: (p * r * t) / 100
p5 = float(input("Enter principal: "))
r5 = float(input("Enter rate: "))
t5 = float(input("Enter time: "))
print("Simple Interest:", simple_interest(p5, r5, t5))





print("\nQuestion 6:")

# 6. Take a list of numbers, use map() and a lambda
# function to generate a list containing their squares.

numbers6 = list(map(int, input("Enter numbers: ").split()))

squares = list(map(lambda n: n * n, numbers6))

print("Squares:", squares)


print("\nQuestion 7:")

# 7. Use map() with lambda to calculate
# the cube of every element in a list.

numbers7 = list(map(int, input("Enter numbers: ").split()))

cubes = list(map(lambda n: n * n * n, numbers7))

print("Cubes:", cubes)


print("\nQuestion 8:")

# 8. Take two lists of numbers, use map() and lambda
# to create a third list containing sum of corresponding elements.

numbers8a = list(map(int, input("Enter first list: ").split()))
numbers8b = list(map(int, input("Enter second list: ").split()))

result8 = list(map(lambda a, b: a + b, numbers8a, numbers8b))

print("Sum of corresponding elements:", result8)





print("\nQuestion 9:")

# 9. Take a list of integers, use filter() and lambda
# to extract all even numbers.

numbers9 = list(map(int, input("Enter numbers: ").split()))

even_numbers = list(filter(lambda n: n % 2 == 0, numbers9))

print("Even numbers:", even_numbers)


print("\nQuestion 10:")

# 10. Take a list of integers, use filter() with
# lambda to identify prime numbers.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers10 = list(map(int, input("Enter numbers: ").split()))

prime_numbers = list(filter(lambda n: is_prime(n), numbers10))

print("Prime numbers:", prime_numbers)


print("\nQuestion 11:")

# 11. Use filter() and lambda to extract
# positive numbers from a list.

numbers11 = list(map(int, input("Enter numbers: ").split()))

positive_numbers = list(filter(lambda n: n > 0, numbers11))

print("Positive numbers:", positive_numbers)


print("\nQuestion 12:")

# 12. Take a list of numbers, use filter() and lambda
# to find numbers greater than 50.

numbers12 = list(map(int, input("Enter numbers: ").split()))

greater_numbers = list(filter(lambda n: n > 50, numbers12))

print("Numbers greater than 50:", greater_numbers)


print("\nQuestion 13:")

# 13. Take a list of words, use filter() and lambda
# to find words having more than five characters.

words13 = input("Enter words: ").split()

long_words = list(filter(lambda word: len(word) > 5, words13))

print("Words having more than 5 characters:", long_words)







print("\nQuestion 14:")

# 14. Take a list of words and sort them
# according to their length using lambda.

words14 = input("Enter words: ").split()

sorted_words = sorted(words14, key=lambda word: len(word))

print("Words sorted according to length:", sorted_words)


print("\nQuestion 15:")

# 15. Take a list of tuples containing student names
# and marks, and sort students according to their marks.

students15 = [
    ("Amit", 85),
    ("Priya", 92),
    ("Rahul", 78),
    ("Sneha", 88)
]

students_sorted = sorted(students15, key=lambda student: student[1])

print("Students sorted according to marks:")

for student in students_sorted:
    print(student)


print("\nQuestion 16:")

# 16. Take employee records containing name and salary,
# and sort them according to salary using lambda.

employees16 = [
    ("Amit", 40000),
    ("Priya", 55000),
    ("Rahul", 45000),
    ("Sneha", 60000)
]

employees_sorted = sorted(employees16, key=lambda employee: employee[1])

print("Employees sorted according to salary:")

for employee in employees_sorted:
    print(employee)







print("\nQuestion 17:")

# 17. Take a list containing student names and marks.
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.

students17 = [
    ("Amit", 85),
    ("Priya", 92),
    ("Rahul", 65),
    ("Sneha", 78),
    ("Rohan", 70)
]


def calculate_average(students):
    total = sum(map(lambda student: student[1], students))
    return total / len(students)


average17 = calculate_average(students17)

above_75 = list(filter(lambda student: student[1] > 75, students17))

sorted_students = sorted(students17, key=lambda student: student[1])


print("Average Marks:", average17)

print("Students scoring above 75:")

for student in above_75:
    print(student)

print("Students sorted according to marks:")

for student in sorted_students:
    print(student)


print("\nQuestion 18:")

# 18. Take employee records containing name, department
# and salary.
# a) Find employees earning more than 50000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.

employees18 = [
    ("Amit", "IT", 45000),
    ("Priya", "HR", 55000),
    ("Rahul", "CSE", 60000),
    ("Sneha", "Finance", 48000)
]


high_salary = list(
    filter(lambda employee: employee[2] > 50000, employees18)
)


increased_salary = list(
    map(lambda employee:
        (employee[0], employee[1], employee[2] * 1.10),
        employees18)
)


sorted_employees = sorted(
    employees18,
    key=lambda employee: employee[2]
)


print("Employees earning more than 50000:")

for employee in high_salary:
    print(employee)


print("Salaries after 10% increase:")

for employee in increased_salary:
    print(employee)


print("Employees sorted according to salary:")

for employee in sorted_employees:
    print(employee)


print("\nQuestion 19:")

# 19. Take a list of products with names, prices and quantities.
# a) Calculate total value of each product.
# b) Filter products costing more than 1000.
# c) Sort products according to total value.
products19 = [
    ("Pen", 20, 10),
    ("Bag", 800, 2),
    ("Laptop", 50000, 1),
    ("Book", 200, 5)
]
def total_value(product):
    return product[1] * product[2]
product_values = list(
    map(lambda product:
        (product[0], product[1], product[2], total_value(product)),
        products19)
)
expensive_products = list(
    filter(lambda product: product[3] > 1000, product_values)
)
sorted_products = sorted(
    product_values,
    key=lambda product: product[3]
)
print("Total value of products:")
for product in product_values:
    print(product)
print("Products costing more than 1000:")
for product in expensive_products:
    print(product)
print("Products sorted according to total value:")
for product in sorted_products:
    print(product)
print("\nQuestion 20:")




# 20. Write a program using functions, map(), filter()
# and lambda expressions to process a list of words.
# a) Find length of every word.
# b) Extract words having more than five characters.
# c) Sort words according to their length.
words20 = input("Enter words: ").split()
def word_length(word):
    return len(word)
lengths20 = list(
    map(lambda word: word_length(word), words20)
)
long_words20 = list(
    filter(lambda word: len(word) > 5, words20)
)
sorted_words20 = sorted(
    words20,
    key=lambda word: len(word)
)
print("Length of every word:", lengths20)
print("Words having more than 5 characters:", long_words20)
print("Words sorted according to length:", sorted_words20)
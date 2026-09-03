print("Question 1:")
# 1. Create a file named student.txt and write student's name, roll number, branch and semester into the file.
file = open("student.txt", "w")
file.write("Name: Purva\n")
file.write("Roll Number: 83\n")
file.write("Branch: CSE\n")
file.write("Semester: 5\n")
file.close()
print("Student details written successfully.")


print("\nQuestion 2:")
# 2. Open a text file and display its complete contents.
file = open("student.txt", "r")
data = file.read()
print("File Contents:")
print(data)
file.close()


print("\nQuestion 3:")
# 3. Append additional student information to an existing file without deleting previous contents.
file = open("student.txt", "a")
file.write("College: DYPCET\n")
file.write("City: Kolhapur\n")
file.close()
print("Additional information appended successfully.")


print("\nQuestion 4:")
# 4. Read a text file line by line and display each line separately.
file = open("student.txt", "r")
for line in file:
    print(line.strip())
file.close()


print("\nQuestion 5:")
# 5. Count and display the total number of lines present in a text file.
file = open("student.txt", "r")
count = 0
for line in file:
    count = count + 1
file.close()
print("Total number of lines:", count)


print("\nQuestion 6:")
# 6. Count the total number of words present in a text file.
file = open("student.txt", "r")
data = file.read()
words = data.split()
print("Total number of words:", len(words))
file.close()


print("\nQuestion 7:")
# 7. Count the total number of characters in a text file,including spaces.
file = open("student.txt", "r")
data = file.read()
print("Total number of characters:", len(data))
file.close()


print("\nQuestion 8:")
# 8. Read a text file and display its lines in reverse order.
file = open("student.txt", "r")
lines = file.readlines()
file.close()
print("Lines in reverse order:")
for line in reversed(lines):
    print(line.strip())


print("\nQuestion 9:")
# 9. Read a text file and count the number of vowels and consonants present in the file.
file = open("student.txt", "r")
data = file.read()
vowels = 0
consonants = 0
for ch in data:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
file.close()
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


print("\nQuestion 10:")
# 10. Read a text file and calculate the number of alphabets, digits, spaces and special characters.
file = open("student.txt", "r")
data = file.read()
alphabets = 0
digits = 0
spaces = 0
special = 0
for ch in data:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    elif ch != "\n":
        special = special + 1
file.close()
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


print("\nQuestion 11:")
# 11. Read a text file and find the longest word present in the file.
file = open("student.txt", "r")
data = file.read()
words = data.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
file.close()
print("Longest word:", longest)


print("\nQuestion 12:")
# 12. Read a text file and count how many times each word occurs. Display the result using a dictionary.
file = open("student.txt", "r")
data = file.read().lower()
words = data.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
file.close()
print("Word occurrences:")
for word, count in word_count.items():
    print(word, ":", count)


print("\nQuestion 13:")
# 13. Accept a word from the user and search for it in a text file. Display occurrences and line numbers.
search_word = input("Enter word to search: ")
file = open("student.txt", "r")
count = 0
line_number = 0
for line in file:
    line_number = line_number + 1
    words = line.split()
    for word in words:
        if word.lower() == search_word.lower():
            count = count + 1
            if line_number not in locals().get("line_numbers", []):
                if "line_numbers" not in locals():
                    line_numbers = []
                line_numbers.append(line_number)
file.close()
print("Number of occurrences:", count)
if count > 0:
    print("Line numbers:", line_numbers)
else:
    print("Word not found.")


print("\nQuestion 14:")
# 14. Read a text file and replace all occurrences of a specified word with another word.
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
file = open("student.txt", "r")
data = file.read()
data = data.replace(old_word, new_word)
file.close()
file = open("student_new.txt", "w")
file.write(data)
file.close()
print("Modified text saved in student_new.txt")


print("\nQuestion 15:")
# 15. Read a Python source file and create another file after removing single-line comments.
file = open("program.py", "r")
lines = file.readlines()
file.close()
new_file = open("program_without_comments.py", "w")
for line in lines:
    if not line.strip().startswith("#"):
        new_file.write(line)
new_file.close()
print("Comments remove successfully.")


print("\nQuestion 16:")
# 16. Read a text file and create another file containing the same text in uppercase.
file = open("student.txt", "r")
data = file.read()
file.close()
new_file = open("uppercase.txt", "w")
new_file.write(data.upper())
new_file.close()
print("Uppercase file created successfully.")

print("\nQuestion 17:")

# 17. Create a file containing student records in the format:
# RollNo,Name,Marks
# Display all records, highest scorer, average marks
# and students scoring more than 80.

file = open("students.txt", "w")

file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

file = open("students.txt", "r")

lines = file.readlines()

file.close()

total_marks = 0
count = 0
highest_marks = 0
highest_name = ""

print("Student Records:")

for line in lines[1:]:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    marks = int(data[2])

    print(roll, name, marks)

    total_marks = total_marks + marks
    count = count + 1

    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

    if marks > 80:
        print("Above 80:", name)

average = total_marks / count

print("Highest Scorer:", highest_name)
print("Highest Marks:", highest_marks)
print("Average Marks:", average)


print("\nQuestion 18:")

# 18. Store employee ID, name, department and salary in a file.
# Display all employees, highest-paid employee,
# average salary and employees above given salary.

file = open("employees.txt", "w")

file.write("101,Amit,IT,40000\n")
file.write("102,Priya,HR,50000\n")
file.write("103,Rahul,CSE,60000\n")
file.write("104,Sneha,Finance,45000\n")

file.close()


def display_employees():
    file = open("employees.txt", "r")

    for line in file:
        print(line.strip())

    file.close()


def highest_paid():
    file = open("employees.txt", "r")

    highest = 0
    highest_name = ""

    for line in file:
        data = line.strip().split(",")

        name = data[1]
        salary = int(data[3])

        if salary > highest:
            highest = salary
            highest_name = name

    file.close()

    print("Highest Paid Employee:", highest_name)
    print("Salary:", highest)


def average_salary():
    file = open("employees.txt", "r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")

        salary = int(data[3])

        total = total + salary
        count = count + 1

    file.close()

    print("Average Salary:", total / count)


def above_salary(amount):
    file = open("employees.txt", "r")

    print("Employees earning above", amount, ":")

    for line in file:
        data = line.strip().split(",")

        name = data[1]
        salary = int(data[3])

        if salary > amount:
            print(name, salary)

    file.close()


print("All Employees:")
display_employees()

highest_paid()

average_salary()

salary18 = int(input("Enter salary: "))
above_salary(salary18)





print("\nQuestion 19:")

# 19. Store student attendance records in a file.
# Calculate attendance percentage and display students
# having attendance below 75%.

file = open("attendance.txt", "w")

file.write("101,Amit,70,100\n")
file.write("102,Priya,85,100\n")
file.write("103,Rahul,60,100\n")
file.write("104,Sneha,90,100\n")

file.close()

file = open("attendance.txt", "r")

print("Students below 75% attendance:")

for line in file:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    present = int(data[2])
    total = int(data[3])

    percentage = (present / total) * 100

    if percentage < 75:
        print(name, ":", percentage, "%")

file.close()


print("\nQuestion 20:")

# 20. Store deposits and withdrawals in a file.
# Calculate total deposits, total withdrawals,
# final balance and largest transaction.

file = open("transactions.txt", "w")

file.write("deposit,5000\n")
file.write("withdrawal,1000\n")
file.write("deposit,3000\n")
file.write("withdrawal,1500\n")

file.close()

file = open("transactions.txt", "r")

total_deposit = 0
total_withdrawal = 0
largest_transaction = 0

for line in file:
    data = line.strip().split(",")

    transaction = data[0]
    amount = int(data[1])

    if transaction == "deposit":
        total_deposit = total_deposit + amount
    else:
        total_withdrawal = total_withdrawal + amount

    if amount > largest_transaction:
        largest_transaction = amount

file.close()

final_balance = total_deposit - total_withdrawal

print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)




print("\nQuestion 21:")

# 21. Maintain book records containing book ID, title,
# author and availability status.
# Implement add, search, issue, return and display operations.

books = {
    101: ["Python", "John", "Available"],
    102: ["Java", "James", "Available"],
    103: ["C++", "Bjarne", "Available"]
}


def add_book(book_id, title, author):
    books[book_id] = [title, author, "Available"]
    print("Book added successfully.")


def search_book(book_id):
    if book_id in books:
        print("Book Found:", books[book_id])
    else:
        print("Book not found.")


def issue_book(book_id):
    if book_id in books:
        if books[book_id][2] == "Available":
            books[book_id][2] = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(book_id):
    if book_id in books:
        books[book_id][2] = "Available"
        print("Book returned successfully.")
    else:
        print("Book not found.")


def display_available():
    print("Available Books:")

    for book_id, details in books.items():
        if details[2] == "Available":
            print(book_id, details)


add_book(104, "DBMS", "Korth")

search_book(101)

issue_book(101)

return_book(101)

display_available()






print("\nQuestion 22:")

# 22. Read the contents of two text files and create
# a third file containing the contents of both files.

file1 = open("file1.txt", "w")
file1.write("This is the content of File 1.\n")
file1.close()

file2 = open("file2.txt", "w")
file2.write("This is the content of File 2.\n")
file2.close()

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

file3 = open("file3.txt", "w")

file3.write(data1)
file3.write(data2)

file3.close()

print("Contents of both files copied to file3.txt")


print("\nQuestion 23:")

# 23. Compare two text files and display whether their
# contents are identical. If different, identify the
# first line where they differ.

file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    minimum = min(len(lines1), len(lines2))

    found = False

    for i in range(minimum):
        if lines1[i] != lines2[i]:
            print("First different line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())

            found = True
            break

    if found == False:
        print("Files have different number of lines.")
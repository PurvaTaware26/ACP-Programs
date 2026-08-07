#Programs of LIST

#Write a Python program to create a list of five fruits and display the list.
print("Question 1:")
list=["Mango","Banana","Grapes","Apple","Orange"]
for i in list:
    print(i)










print("\nQuestion 2:")
#2.	Create a list of five integers. Display:first element, last element, and third element of the list.
list=[10,20,30,40,50]
print("First element:",list[0])
print("Last element:",list[-1])
print("Third element:",list[2])












print("\nQuestion 3:")
#3.	Create a list of colors. Replace the third color with another color and display the updated list.
list=["Red","Green","Blue","Yellow","Purple"]
list[2]="Pink"
print("Updated list:",list)








print("\nQuestion 4:")
#4.	Create a list of numbers. Add: one element at the end, one element at the beginning, and one element at a specified position. Display the updated list.
list=[20,30,40,50,60]
list.append(70)
list.insert(0,10)
list.insert(3,35)
print("Updated list:",list)











print("\nQuestion 5:")
#5.	Create a list of student names. Remove:first student, last student, and a specific student by name. Display the updated list.
list=["Ketan","Rahul","Chetan","Isha","Arya"]
list.pop(0)  # Remove first student
list.pop(-1)  # Remove last student
list.remove("Chetan")  # Remove specific student by name
print("Updated list:", list)











print("\nQuestion 6:")
#6.Write a program to find the largest and smallest number in a list without using max() or min().
list=[10,20,5,30,15]
largest=list[0]
smallest=list[0]
for num in list:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print("Largest number:",largest)
print("Smallest number:",smallest)









print("\nQuestion 7:")
#7.	Accept 10 numbers from the user and store them in a list. Calculate:sum and average of the numbers. 
list=[]
print("enter 10 numbers")
for i in range(10):
    num=int(input("Enter number:"))
    list.append(num)
    
sum=0
for num in list:
    sum+=num
average=sum/10
print("Sum:",sum)
print("Average:",average)














print("\nQuestion 8:")
#8.	Store 15 integers in a list. Count how many numbers are:even and how many are odd.
list=[]
for i in range(15):
    num=int(input("Enter number:"))
    list.append(num)    
even_count=0
odd_count=0
for num in list:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even numbers:",even_count)
print("Odd numbers:",odd_count)












print("\nQuestion 9:")
#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
List=["Mumbai","Delhi","Bangalore","Chennai","Kolkata"]
city=input("Enter city name:")
if city in List:
    print("City exists in the list.")
else:
    print("City does not exist in the list.")









print("\nQuestion 10:")
#10.	Write a program to reverse a list without using the reverse() method.
List=[1,2,3,4,5]
reversed_list=[]
for i in range(len(List)-1,-1,-1):
    reversed_list.append(List[i])
print("Reversed list:",reversed_list)











print("\nQuestion 11:")
#11.	Create a list of 10 numbers and display:First 5 elements, Last 5 elements, Middle 4 elements, Alternate elements, Reverse list using slicing.
List=[10,20,30,40,50,60,70,80,90,100]
print("First 5 elements:",List[:5])
print("Last 5 elements:",List[-5:])
middle_index=len(List)//2
print("Middle 4 elements:",List[middle_index-2:middle_index+2])
print("Alternate elements:",List[::2])
print("Reverse list using slicing:",List[::-1])











print("\nQuestion 12:")
#12.	Display all elements present at even index positions.
List=[10,20,30,40,50,60,70,80,90,100]
print("Elements at even index positions:",List[::2])








    
print("\nQuestion 13:")
#13.	Accept 10 numbers and sort them in:Ascending and descending order
numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = int(input())
    numbers.append(num)
ascending = sorted(numbers)
print("Ascending order:", ascending)
descending = sorted(numbers, reverse=True)
print("Descending order:", descending)
    






print("\nQuestion 14:")
#14.	Create a list containing duplicate values and display only unique elements.
numbers1 = [10, 20, 30, 20, 40, 10, 50, 30, 60]
unique = []
for i in numbers1:
    if i not in unique:
        unique.append(i)
print("Original List:", numbers1)
print("Unique Elements:", unique)






print("\nQuestion 15:")
#15.	Find the second largest element in a list.
element_list = [12, 45, 67, 23, 89, 54]
element_list.sort()
print("Second Largest Element:", element_list[-2])




print("\nQuestion 16:")
#16.	Create a nested list storing: student Name,Roll Number,Marks. Display all student details.
student_details = [
    ["Amit", 101, 85],
    ["Priya", 102, 90],
    ["Rahul", 103, 78]
]
print("Student Details")
for stud in student_details:
    print("Name :", stud[0])
    print("Roll Number :", stud[1])
    print("Marks :", stud[2])
    print()




print("\nQuestion 17:")
#17.Create two 3 × 3 matrices using nested lists and perform matrix addition.
matrix_one = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_two = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
addition_result = []
for row_value in range(3):
    current_row = []
    for column_value in range(3):
        current_row.append(matrix_one[row_value][column_value] + matrix_two[row_value][column_value])
    addition_result.append(current_row)
print("Matrix Addition:")
for result_row in addition_result:
    print(result_row)







print("\nQuestion 18:")
#18.	Create a shopping cart using a list.Perform: Add item,remove item, search item, display cart, count total items.
shopping_items = ["Milk", "Bread", "Butter"]

shopping_items.append("Eggs")
print("After Adding Item:", shopping_items)

shopping_items.remove("Bread")
print("After Removing Item:", shopping_items)

search_product = "Milk"

if search_product in shopping_items:
    print(search_product, "is Found")
else:
    print(search_product, "is Not Found")


print("Shopping Cart:", shopping_items)


print("Total Items:", len(shopping_items))








print("\nQuestion 19:")
#19.	Store names of students present in class.Display total students,search a student attendance,add a new student,remove an absent student
present_students = ["Amit", "Priya", "Rahul"]
print("Total Students:", len(present_students))

student_name = "Priya"

if student_name in present_students:
    print(student_name, "is Present")
else:
    print(student_name, "is Absent")

present_students.append("Sneha")
print("After Adding Student:", present_students)

present_students.remove("Rahul")
print("After Removing Student:", present_students)








print("\nQuestion 20:")
#20.	Create a list of books.Add a new book ,search a book,remove a book,display all books,count total books
book_list = ["Python", "Java", "C++"]
book_list.append("Data Science")
print("After Adding Book:", book_list)


book_name = "Java"

if book_name in book_list:
    print(book_name, "is Available")
else:
    print(book_name, "is Not Available")


book_list.remove("C++")
print("After Removing Book:", book_list)

print("Book List:", book_list)
print("Total Books:", len(book_list))









print("\nQuestion 21:")
#21.	Accept two lists and merge them into a single list.
first_list = [10, 20, 30]
second_list = [40, 50, 60]

merged_list = first_list + second_list

print("First List:", first_list)
print("Second List:", second_list)
print("Merged List:", merged_list)








print("\nQuestion 22:")
#22.	Find common elements between two lists.
list_one = [10, 20, 30, 40, 50]
list_two = [30, 40, 50, 60, 70]

common_elements = []

for value in list_one:
    if value in list_two:
        common_elements.append(value)

print("First List:", list_one)
print("Second List:", list_two)
print("Common Elements:", common_elements)








print("\nQuestion 23:")
#23.	Count the frequency of each element in a list.
number_collection = [10, 20, 10, 30, 20, 10, 40]

checked_elements = []

for current_element in number_collection:
    if current_element not in checked_elements:
        frequency = number_collection.count(current_element)
        print(current_element, "appears", frequency, "times")
        checked_elements.append(current_element)








print("\nQuestion 24:")
#24.	Rotate a list:left by one position,right by one position
rotate_values = [10, 20, 30, 40, 50]

left_rotation = rotate_values[1:] + [rotate_values[0]]
print("Left Rotation :", left_rotation)
right_rotation = [rotate_values[-1]] + rotate_values[:-1]
print("Right Rotation:", right_rotation)








print("\nQuestion 25:")
#25.	Remove all duplicate elements while preserving the original order.
original_numbers = [10, 20, 30, 20, 40, 10, 50, 30]
unique_numbers = []
for current_value in original_numbers:
    if current_value not in unique_numbers:
        unique_numbers.append(current_value)

print("Original List:", original_numbers)
print("List After Removing Duplicates:", unique_numbers)










print("\nQuestion 26:")
#26.Store marks of 20 students in a list and determine:highest marks,lowest marks,average marks,number of students scoring above average,number of students scoring below average.
student_marks = [75, 82, 68, 90, 55, 77, 88, 92, 64, 70,
                 81, 73, 69, 95, 60, 84, 79, 66, 87, 72]

highest_marks = max(student_marks)
lowest_marks = min(student_marks)

total_marks = sum(student_marks)
average_marks = total_marks / len(student_marks)

above_average = 0
below_average = 0

for marks_value in student_marks:
    if marks_value > average_marks:
        above_average += 1
    elif marks_value < average_marks:
        below_average += 1

print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", average_marks)
print("Students Scoring Above Average:", above_average)
print("Students Scoring Below Average:", below_average)












print("\nQuestion 27:")
#27.Store salaries of employees and determine:Highest salary,lowest salary,average salary,employees earning above 50,000,employees earning below 30000
employee_salaries = [25000, 32000, 48000, 55000, 62000, 28000, 75000, 45000, 52000, 29000]

highest_salary = max(employee_salaries)
lowest_salary = min(employee_salaries)

total_salary = sum(employee_salaries)
average_salary = total_salary / len(employee_salaries)

above_50000 = 0
below_30000 = 0

for salary_amount in employee_salaries:
    if salary_amount > 50000:
        above_50000 += 1
    if salary_amount < 30000:
        below_30000 += 1

print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)
print("Average Salary:", average_salary)
print("Employees Earning Above 50000:", above_50000)
print("Employees Earning Below 30000:", below_30000)









print("\nQuestion 28:")
#28.Store scores of a batsman in 10 matches and calculate:Highest score,lowest score,total runs,average runs,number of centuries,number of half centuries
match_scores = [45, 102, 67, 120, 89, 34, 56, 150, 78, 99]

highest_score = max(match_scores)
lowest_score = min(match_scores)

total_runs = sum(match_scores)
average_runs = total_runs / len(match_scores)

centuries = 0
half_centuries = 0

for score_value in match_scores:
    if score_value >= 100:
        centuries += 1
    elif score_value >= 50:
        half_centuries += 1

print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Total Runs:", total_runs)
print("Average Runs:", average_runs)
print("Number of Centuries:", centuries)
print("Number of Half Centuries:", half_centuries)











print("\nQuestion 29:")
#29.	Store the temperature of 30 days and determine:	Hottest day ,Coldest day ,	Average temperature,Days above average temperature ,Days below average temperature
daily_temperatures = [30, 32, 31, 33, 35, 36, 34, 32, 31, 30,
                      29, 28, 30, 31, 33, 35, 36, 37, 34, 32,
                      31, 30, 29, 28, 27, 29, 31, 33, 34, 35]

hottest_day = max(daily_temperatures)
coldest_day = min(daily_temperatures)

total_temperature = sum(daily_temperatures)
average_temperature = total_temperature / len(daily_temperatures)

above_average_days = 0
below_average_days = 0
for temperature_value in daily_temperatures:
    if temperature_value > average_temperature:
        above_average_days += 1
    elif temperature_value < average_temperature:
        below_average_days += 1

print("Hottest Day Temperature:", hottest_day)
print("Coldest Day Temperature:", coldest_day)
print("Average Temperature:", average_temperature)
print("Days Above Average Temperature:", above_average_days)
print("Days Below Average Temperature:", below_average_days)











print("\nQuestion 30

:")
#30.	Store patient names and ages using lists.Add patient,delete patient,search patient,display all patients,count total patients.
patient_names = ["Amit", "Priya", "Rahul"]
patient_ages = [35, 28, 42]


patient_names.append("Sneha")
patient_ages.append(30)
print("After Adding Patient:")
for patient_index in range(len(patient_names)):
    print(patient_names[patient_index], "-", patient_ages[patient_index])


delete_patient = "Rahul"
if delete_patient in patient_names:
    patient_position = patient_names.index(delete_patient)
    patient_names.pop(patient_position)
    patient_ages.pop(patient_position)

print("\nAfter Deleting Patient:")
for patient_index in range(len(patient_names)):
    print(patient_names[patient_index], "-", patient_ages[patient_index])
search_patient = "Priya"
if search_patient in patient_names:
    print("\n", search_patient, "Found")
else:
    print("\n", search_patient, "Not Found")

print("\nPatient List:")
for patient_index in range(len(patient_names)):
    print(patient_names[patient_index], "-", patient_ages[patient_index])

print("\nTotal Patients:", len(patient_names))






#1.	Write a Python program to create a tuple of five integers and display it.
print("Question 1:")
tuple1=(1, 2, 3, 4, 5)
print(tuple1)

print("\nQuestion 2:")
#2.	Create a tuple containing five city names. Display:
#First city 
#Last city 
#Third city
city_tuple=("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print("First city:", city_tuple[0])
print("Last city:", city_tuple[-1])
print("Third city:", city_tuple[2])

print("\nQuestion 3:")
#3.	Write a Python program to create a tuple with different data types and display it.
mixed_tuple=(1, "Hello", 3.14, True, [1, 2, 3])
print(mixed_tuple)


print("\nQuestion 4:")
#4. Create a tuple of colors. Check whether a given color exists in the tuple.
color_tuple=("Red", "Blue", "Green", "Yellow", "Black")
color=input("Enter a color: ")
if color in color_tuple:
    print("Color exists in the tuple")
else:
    print("Color does not exist in the tuple")









print("\nQuestion 5:")
#5. Create a tuple of fruits and display each fruit using a loop.
fruit_tuple=("Apple", "Banana", "Mango", "Orange", "Grapes")
for fruit in fruit_tuple:
    print(fruit)










print("\nQuestion 6:")
#6. Create a tuple with repeated numbers and count how many times a particular number appears.
number_tuple=(1, 2, 3, 2, 4, 2, 5, 2, 6)
number=2
count=number_tuple.count(number)
print("Number of times", number, "appears:", count)







print("\nQuestion 7:")
#7. Create a tuple of employee IDs and find the index of a given ID.
employee_tuple=(101, 102, 103, 104, 105)
id=103
index=employee_tuple.index(id)
print("Index of employee ID", id, "is:", index)







print("\nQuestion 8:")
#8. Create two tuples of numbers and concatenate them into a single tuple.
tuple1=(1, 2, 3)
tuple2=(4, 5, 6)
tuple3=tuple1+tuple2
print("Combined tuple:", tuple3)


print("\nQuestion 9:")
#9. Create a tuple containing three elements and repeat it four times.
tuple1=("A", "B", "C")
tuple2=tuple1*4
print("Repeated tuple:", tuple2)





print("\nQuestion 10:")
#10. Create a tuple of 10 numbers and display:
#First five elements
#Last five elements
#Middle four elements
#Alternate elements
#Reverse tuple
number_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five elements:", number_tuple[:5])
print("Last five elements:", number_tuple[5:])
print("Middle four elements:", number_tuple[3:7])
print("Alternate elements:", number_tuple[::2])
print("Reverse tuple:", number_tuple[::-1])








print("\nQuestion 11:")
#11. Convert a tuple into a list and add a new element.
tuple1=(10, 20, 30, 40)
list1=list(tuple1)
list1.append(50)
print("List after adding new element:", list1)








print("\nQuestion 12:")
#12. Accept five numbers from the user, store them in a list, and convert the list into a tuple.
list1=[]
for i in range(5):
    number=int(input("Enter a number: "))
    list1.append(number)
tuple1=tuple(list1)
print("Tuple:", tuple1)








print("\nQuestion 13:")
#13. Modify a tuple by converting it into a list and then back into a tuple.
tuple1=(10, 20, 30, 40)
list1=list(tuple1)
list1[1]=50
tuple1=tuple(list1)
print("Modified tuple:", tuple1)










print("\nQuestion 14:")
#14. Create a tuple and delete it completely.
tuple1=(10, 20, 30, 40)
print("Tuple before deleting:", tuple1)
del tuple1
print("Tuple deleted successfully")








print("\nQuestion 15:")
#15. Create a nested tuple containing student details and display each record.
student_tuple=(
    (1, "Rahul", "CSE"),
    (2, "Priya", "IT"),
    (3, "Amit", "CSE")
)

for student in student_tuple:
    print(student)
  


  
print("\nQuestion 16:")
#16. Store ten numbers in a tuple and calculate their sum.
number_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sum1=0
for number in number_tuple:
    sum1=sum1+number
print("Sum:", sum1)


print("\nQuestion 17:")
#17. Find the largest and smallest number in a tuple without using max() and min().
number_tuple=(10, 25, 5, 40, 15)
largest=number_tuple[0]
smallest=number_tuple[0]
for number in number_tuple:
    if number>largest:
        largest=number
    if number<smallest:
        smallest=number
print("Largest number:", largest)
print("Smallest number:", smallest)







print("\nQuestion 18:")
#18. Calculate the average of elements stored in a tuple.
number_tuple=(10, 20, 30, 40, 50)
sum1=0
for number in number_tuple:
    sum1=sum1+number
average=sum1/len(number_tuple)
print("Average:", average)
print("\nQuestion 19:")








#19. Store 15 integers in a tuple and count:
#Even numbers
#Odd numbers
number_tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even=0
odd=0
for number in number_tuple:
    if number%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even numbers:", even)
print("Odd numbers:", odd)






print("\nQuestion 20:")
#20. Accept a number from the user and determine whether it exists in the tuple.
number_tuple=(10, 20, 30, 40, 50)
number=int(input("Enter a number: "))
if number in number_tuple:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")





print("\nQuestion 21:")
#21. Store student details in a tuple:
#Roll Number
#Name
#Department
#Marks
#Display all the details.
student=(101, "Rahul", "CSE", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])










print("\nQuestion 22:")
#22. Create tuples containing:
#Employee ID
#Name
#Salary
#Display all employee information.
employee1=(101, "Rahul", 25000)
employee2=(102, "Priya", 30000)
employee3=(103, "Amit", 28000)
print("Employee 1:", employee1)
print("Employee 2:", employee2)
print("Employee 3:", employee3)







print("\nQuestion 23:")
#23. Store item prices in a tuple and calculate:
#Total bill
#Average price
#Highest-priced item
#Lowest-priced item
price_tuple=(100, 250, 150, 300, 200)
sum1=0
for price in price_tuple:
    sum1=sum1+price
average=sum1/len(price_tuple)
highest=price_tuple[0]
lowest=price_tuple[0]
for price in price_tuple:
    if price>highest:
        highest=price

    if price<lowest:
        lowest=price
print("Total bill:", sum1)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)













print("\nQuestion 24:")
#24. Store temperatures of seven days in a tuple and determine:
#Maximum temperature
#Minimum temperature
#Average temperature
temperature_tuple=(30, 32, 29, 31, 33, 28, 30)
sum1=0
for temperature in temperature_tuple:
    sum1=sum1+temperature
maximum=temperature_tuple[0]
minimum=temperature_tuple[0]
for temperature in temperature_tuple:
    if temperature>maximum:
        maximum=temperature

    if temperature<minimum:
        minimum=temperature
average=sum1/len(temperature_tuple)
print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)









print("\nQuestion 25:")
#25. Store runs scored in 10 matches and calculate:
#Total runs
#Highest score
#Lowest score
#Average score
runs=(45, 67, 23, 89, 56, 34, 78, 90, 12, 50)
sum1=0
for run in runs:
    sum1=sum1+run
highest=runs[0]
lowest=runs[0]
for run in runs:
    if run>highest:
        highest=run
    if run<lowest:
        lowest=run
average=sum1/len(runs)
print("Total runs:", sum1)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)







print("\nQuestion 26:")
#26. Create two tuples and find the common elements between them.
tuple1=(1, 2, 3, 4, 5)
tuple2=(3, 4, 5, 6, 7)
print("Common elements:")
for number in tuple1:
    if number in tuple2:
        print(number)






print("\nQuestion 27:")
#27. Merge two tuples and remove duplicate elements.
tuple1=(1, 2, 3, 4)
tuple2=(3, 4, 5, 6)
tuple3=tuple1+tuple2
list1=[]
for number in tuple3:
    if number not in list1:
        list1.append(number)
tuple4=tuple(list1)
print("Merged tuple:", tuple4)










print("\nQuestion 28:")
#28. Count the frequency of each element in a tuple.
tuple1=(1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
list1=[]
for number in tuple1:
    if number not in list1:
        print(number, "appears", tuple1.count(number), "times")
        list1.append(number)







print("\nQuestion 29:")
#29. Convert a tuple into a sorted tuple in ascending and descending order.
tuple1=(5, 2, 8, 1, 9, 3)
list1=list(tuple1)
list1.sort()
ascending=tuple(list1)
list1.sort(reverse=True)
descending=tuple(list1)
print("Ascending order:", ascending)
print("Descending order:", descending)









print("\nQuestion 30:")
#30. Create a tuple containing patient records:
#Patient ID
#Name
#Age
#Blood Group
patient_tuple=(
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 22, "A+"),
    (104, "Sneha", 28, "O+")
)
print("All patient records:")
for patient in patient_tuple:
    print(patient)
id=int(input("Enter patient ID to search: "))
found=False
for patient in patient_tuple:
    if patient[0]==id:
        print("Patient found:", patient)
        found=True
if found==False:
    print("Patient not found")
#Count the total number of patients
print("Total number of patients:", len(patient_tuple))
blood_group=input("Enter blood group: ")
print("Patients with blood group", blood_group, ":")
for patient in patient_tuple:
    if patient[3]==blood_group:
        print(patient)
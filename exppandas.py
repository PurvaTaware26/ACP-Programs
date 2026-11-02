import pandas as pd

# Question 1: Create a dictionary containing information for 5 students. Convert it into a DataFrame, calculate total and average marks, and display students with average marks greater than 75.

students = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Python": [85, 70, 90, 60, 95],
    "DBMS": [80, 75, 85, 65, 90],
    "Mathematics": [90, 80, 88, 70, 92]
}

df = pd.DataFrame(students)
df["Total_Marks"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average_Marks"] = df["Total_Marks"] / 3

print(df)
print("Students with average marks greater than 75:")
print(df[df["Average_Marks"] > 75])


# Question 2: Create an employee dictionary, convert it into a DataFrame, display employees with salary greater than ₹50,000, find average salary, highest salary, and employee with highest experience.

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "CSE", "HR", "IT"],
    "Salary": [45000, 60000, 75000, 40000, 80000],
    "Experience": [2, 5, 7, 3, 8]
}

df = pd.DataFrame(employees)

print(df)
print("Employees with salary greater than ₹50,000:")
print(df[df["Salary"] > 50000])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])


# Question 3: Create a product dictionary, convert it into a DataFrame, calculate Total Amount = Price × Quantity, and find the product with the highest total sales.

products = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 20000, 1500, 12000, 500],
    "Quantity": [3, 5, 10, 4, 20]
}

df = pd.DataFrame(products)
df["Total_Amount"] = df["Price"] * df["Quantity"]

print(df)
print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# Question 4: Create a patient dictionary, convert it into a DataFrame, display patients above 60 years, find average and maximum medical charges, and display patients whose medical charges exceed ₹50,000.

patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Cancer"],
    "Medical_Charges": [60000, 15000, 90000, 20000, 75000]
}

df = pd.DataFrame(patients)

print(df)
print("Patients above 60 years:")
print(df[df["Age"] > 60])
print("Average Medical Charges:", df["Medical_Charges"].mean())
print("Maximum Medical Charges:", df["Medical_Charges"].max())
print("Patients with charges greater than ₹50,000:")
print(df[df["Medical_Charges"] > 50000])


# Question 5: Create an order dictionary, calculate Final Amount = Quantity × Price − Discount, and display all orders, orders above ₹5,000, highest-value order, and average order value.

orders = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [2, 3, 4, 2, 1],
    "Price": [50000, 20000, 12000, 15000, 8000],
    "Discount": [5000, 2000, 1000, 500, 500]
}

df = pd.DataFrame(orders)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("All Orders:")
print(df)
print("Orders above ₹5,000:")
print(df[df["Final_Amount"] > 5000])
print("Highest-value Order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("Average Order Value:", df["Final_Amount"].mean())


# Question 6: Create a student attendance dictionary, calculate Attendance Percentage = (Classes_Attended / Total_Classes) × 100, and display students whose attendance is below 75%.

attendance = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [85, 70, 90, 60, 55]
}

df = pd.DataFrame(attendance)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)
print("Students with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# Question 7: Create a retail sales dictionary, convert it into a DataFrame, add Total_Sales = Price × Quantity, display products with sales greater than ₹10,000, find maximum sales, and calculate average sales.

products = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 20000, 1500, 12000, 500],
    "Quantity": [2, 4, 5, 3, 10]
}

df = pd.DataFrame(products)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print(df)
print("Products with sales greater than ₹10,000:")
print(df[df["Total_Sales"] > 10000])
print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("Average Sales:", df["Total_Sales"].mean())


# Question 8: Create a Pandas Series using a dictionary of student names and marks. Display the Series, marks of a particular student, maximum and minimum marks, average marks, and students scoring more than 75.

marks = {
    "Amit": 85,
    "Priya": 92,
    "Rahul": 68,
    "Sneha": 78,
    "Neha": 95
}

s = pd.Series(marks)

print(s)
print("Marks of Priya:", s["Priya"])
print("Maximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())
print("Students scoring more than 75:")
print(s[s > 75])


# Question 9: Create a Pandas Series using employee names and salaries. Display the Series, highest and lowest salary, average salary, and employees earning more than ₹50,000.

salaries = {
    "Amit": 45000,
    "Priya": 60000,
    "Rahul": 75000,
    "Sneha": 40000,
    "Neha": 80000
}

s = pd.Series(salaries)

print(s)
print("Highest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())
print("Employees earning more than ₹50,000:")
print(s[s > 50000])


# Question 10: Create a Pandas Series using product names and prices. Display all products and prices, increase every price by 10%, find the most expensive product, and display products costing more than ₹1,000.

prices = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Mouse": 500
}

s = pd.Series(prices)

print("Products and Prices:")
print(s)
s = s * 1.10
print("Prices after 10% increase:")
print(s)
print("Most Expensive Product:")
print(s.idxmax(), s.max())
print("Products costing more than ₹1,000:")
print(s[s > 1000])


# Question 11: Create a Pandas Series using patient IDs as the index and patient ages as values. Find average age, oldest and youngest patients, and display patients above 60 years.

ages = {
    101: 65,
    102: 45,
    103: 72,
    104: 30,
    105: 61
}

s = pd.Series(ages)

print("Average Age:", s.mean())
print("Oldest Patient:", s.idxmax(), s.max())
print("Youngest Patient:", s.idxmin(), s.min())
print("Patients above 60 years:")
print(s[s > 60])


# Question 12: Create a Pandas Series using student names and attendance percentages. Find average attendance, display students below 75% and above 90%, and find highest attendance.

attendance = {
    "Amit": 85,
    "Priya": 95,
    "Rahul": 68,
    "Sneha": 72,
    "Neha": 98
}

s = pd.Series(attendance)

print("Average Attendance:", s.mean())
print("Students with attendance below 75%:")
print(s[s < 75])
print("Students with attendance above 90%:")
print(s[s > 90])
print("Highest Attendance:", s.max())
print("Student with highest attendance:", s.idxmax())


# Question 13: Read students.csv using Pandas. Display the first and last 5 records, total and average marks of each student, students with average above 75, student with highest average, and average marks for each subject.

df = pd.read_csv("students.csv")

print("First 5 Records:")
print(df.head())
print("Last 5 Records:")
print(df.tail())

df["Total_Marks"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average_Marks"] = df["Total_Marks"] / 3

print("Total and Average Marks:")
print(df)
print("Students with average marks greater than 75:")
print(df[df["Average_Marks"] > 75])
print("Student with highest average:")
print(df.loc[df["Average_Marks"].idxmax()])
print("Average Marks for Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


# Question 14: Read employees.csv using Pandas. Display employees from the CSE department, average salary, highest and lowest salary, employees earning more than ₹50,000, and department-wise average salary.

df = pd.read_csv("employees.csv")

print("Employees from CSE Department:")
print(df[df["Department"] == "CSE"])
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("Employees earning more than ₹50,000:")
print(df[df["Salary"] > 50000])
print("Department-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


# Question 15: Read patients.csv using Pandas. Display patients above 60 years, average medical expense, patient with highest medical expense, disease-wise patient count, and patients whose medical expense exceeds ₹50,000.

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])
print("Average Medical Expense:", df["Medical_Expense"].mean())
print("Patient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])
print("Count of Patients for Each Disease:")
print(df["Disease"].value_counts())
print("Patients with medical expense greater than ₹50,000:")
print(df[df["Medical_Expense"] > 50000])


# Question 16: Read weather.csv using Pandas. Find maximum, minimum, and average temperature, display records where temperature is above 35°C, and calculate city-wise average temperature.

df = pd.read_csv("weather.csv")

print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())
print("Average Temperature:", df["Temperature"].mean())
print("Records with temperature above 35°C:")
print(df[df["Temperature"] > 35])
print("City-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())
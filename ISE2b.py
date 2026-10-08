import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Vijay"],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
}
df = pd.DataFrame(data)
def highest_salary(df):
    employee = df.loc[df["Salary"].idxmax()]
    print("Highest Paid Employee:")
    print(employee)

def department_average(df):
    average = df.groupby("Department")["Salary"].mean()
    print("\nDepartment-wise Average Salary:")
    print(average)


def salary_ranking(df):
    df["Rank"] = df["Salary"].rank(ascending=False, method="min")
    print("\nSalary Ranking:")
    print(df[["Name", "Salary", "Rank"]].sort_values("Rank"))


highest_salary(df)
department_average(df)
salary_ranking(df)
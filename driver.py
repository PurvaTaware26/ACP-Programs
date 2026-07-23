married=input("Enter  (married/unmarried): ").lower()
if married=="married":
    print("Driver is Insured.")
else:
    gender=input("Enter gender (male/female): ").lower()
    age=int(input("Enter age: "))
    if (gender == "male" and age > 30) or (gender == "female" and age > 25):
        print("Driver is Insured.")
    else:
        print("Driver is Not Insured.")
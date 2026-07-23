mark1=int(input("enter the marks obtained in english: "))
mark2=int(input("enter the marks obtained in maths: "))
mark3=int(input("enter the marks obtained in science: "))
mark4=int(input("enter the marks obtained in IT:"))
total=mark1+mark2+mark3+mark4
percent=(total/400)*100
print("Percent: ",percent)
if percent>=90:
    print("Excellent performance")
elif percent>=80:
    print("Very Good performance")
elif percent>=70:
    print("Good performance")
elif percent>=60:
    print("average performance")
else:
    print("Poor performance")    









#Programs of FOR LOOP




print("\nQuestion1: ")
#1.Write a PYTHON program to print the natural numbers up to n
n = int(input("Enter the value of n: "))
print("Natural numbers up to", n, "are:")
for i in range(1, n + 1):
    print(i)





print("\nQuestion2: ")
#2.Write a PYTHON program to print even numbers up to n

n1 = int(input("Enter the value of n: "))

print("Even numbers up to", n1, "are:")

for i in range(2, n1 + 1, 2):
    print(i)






print("\nQuestion3: ")
#3.Write a PYTHON program to print odd numbers up to n
n2 = int(input("Enter the value of n: "))
print("Odd numbers up to", n2, "are:")
for i in range(1, n2 + 1, 2):
    print(i)





print("\nQuestion4: ")
#4.Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n3 = int(input("Enter the value of n: "))
i = 1
while i <= n3 * n3:
    print(i, end=" ")
    i = i * 2





print("\nQuestion5: ")
#5.Write a PYTHON program to sum the given sequence
     # 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n4 = int(input("Enter the value of n: "))
sum = 1
fact = 1
for i in range(1, n4 + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum of the series =", sum)






print("\nQuestion6: ")
#6.  Write a PYTHON program to compute the cosine series
          #cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!
x = float(input("Enter the value of x: "))
n5 = int(input("Enter the value of n (even): "))

sum = 1
fact = 1
sign = -1

for i in range(2, n5 + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + sign * (x ** i) / fact
    sign = sign * -1

print("Value of cosine series =", sum)






print("\nQuestion7: ")
#7.  Write a short PYTHON program to check weather the 
     #square root of number is prime or  not
# 7. Python program to check whether the square root
# of a number is prime or not

num = int(input("Enter a number: "))

root = int(num ** 0.5)

count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count = count + 1

if count == 2:
    print("Square root =", root)
    print("Square root is Prime")
else:
    print("Square root =", root)
    print("Square root is Not Prime")






print("\nQuestion8: ")
#8.  Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 

for i in range(3):
    for ch in "ABC":
        print(ch, end=" ")
    print()








print("\nQuestion9: ")
#9.  Write a PYTHON program to produce following design
      #A
      #A B
      #A B C
      #A B C D 
      #A B C D E
      #If user enters n value as 5

n6 = int(input("Enter the value of n: "))

for i in range(1, n6 + 1):
    for ch in "ABCDE"[:i]:
        print(ch, end=" ")
    print()







print("\nQuestion10: ")
#10. Write a PYTHON program to produce following design
       #A B C D E
       #A B C D
       #A B C
       #A B
       #A                      
      #(If user enters n value as 5)
n7 = int(input("Enter the value of n: "))

for i in range(n7, 0, -1):
    for ch in "ABCDE"[:i]:
        print(ch, end=" ")
    print()






print("\nQuestion11: ")
#11. Write a PYTHON program to produce following  
      #1
      #1 2
      #1 2 3
      #1 2 3 4
      #1 2 3 4 5
      #If user enters n value as 5
n8 = int(input("Enter the value of n: "))

for i in range(1, n8 + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()







print("\nQuestion12: ")
#12. Write a PYTHON program to produce following design
      #1
      #2 2
      #3 3 3
      #4 4 4 4 
      #5 5 5 5 5
      #If user enters n value as 5
n9 = int(input("Enter the value of n: "))

for i in range(1, n9 + 1):
    for j in range(i):
        print(i, end=" ")
    print()





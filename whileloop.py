#Programs of WHILE LOOP



print("\nQuestion1: ")
#1. Write a PYTHON program to print the natural numbers up to n

n = int(input("Enter the value of n: "))

print("Natural numbers up to", n, "are:")

i = 1
while i <= n:
    print(i)
    i = i + 1









print("\nQuestion2: ")
#2. Write a PYTHON program to print even numbers up to n

n1 = int(input("Enter the value of n: "))

print("Even numbers up to", n1, "are:")

i = 2
while i <= n1:
    print(i)
    i = i + 2







print("\nQuestion3: ")
#3. Write a PYTHON program to print odd numbers up to n

n2 = int(input("Enter the value of n: "))

print("Odd numbers up to", n2, "are:")

i = 1
while i <= n2:
    print(i)
    i = i + 2










print("\nQuestion4: ")
#4. Write a PYTHON program to print sum of natural numbers up to n
n3 = int(input("Enter the value of n: "))

i = 1
sum = 0

while i <= n3:
    sum = sum + i
    i = i + 1

print("Sum of natural numbers =", sum)










print("\nQuestion5: ")
#5. Write a PYTHON program to print sum of odd numbers up to n

n4 = int(input("Enter the value of n: "))

i = 1
sum = 0

while i <= n4:
    sum = sum + i
    i = i + 2

print("Sum of odd numbers =", sum)













print("\nQuestion6: ")
#6. Write a PYTHON program to print sum of even numbers up to n

n5 = int(input("Enter the value of n: "))

i = 2
sum = 0

while i <= n5:
    sum = sum + i
    i = i + 2

print("Sum of even numbers =", sum)










print("\nQuestion7: ")
#7. Write a PYTHON program to print natural numbers up to n in reverse order

n6 = int(input("Enter the value of n: "))

print("Natural numbers in reverse order are:")

i = n6

while i >= 1:
    print(i)
    i = i - 1












print("\nQuestion8: ")
#8. Write a PYTHON program to print Fibonacci series up to n

n7 = int(input("Enter the value of n: "))

a = 0
b = 1
count = 1

print("Fibonacci series:")

while count <= n7:
    print(a)
    c = a + b
    a = b
    b = c
    count = count + 1










print("\nQuestion9: ")
#9. Write a PYTHON program to find factorial of given number

n8 = int(input("Enter the value of n: "))

fact = 1
i = 1

while i <= n8:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)










print("\nQuestion10: ")
#10. Write a PYTHON program to check the entered number is prime or not

n9 = int(input("Enter the value of n: "))

i = 1
count = 0

while i <= n9:
    if n9 % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print(n9, "is Prime")
else:
    print(n9, "is Not Prime")










print("\nQuestion11: ")
#11. Write a PYTHON program to find the sum of digits of given number

n10 = int(input("Enter the value of n: "))

sum = 0

while n10 > 0:
    digit = n10 % 10
    sum = sum + digit
    n10 = n10 // 10

print("Sum of digits =", sum)











print("\nQuestion12: ")
#12. Write a PYTHON program to check the entered number is palindrome or not
n11 = int(input("Enter the value of n: "))
temp = n11
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if rev == n11:
    print(n11, "is Palindrome")
else:
    print(n11, "is Not Palindrome")










print("\nQuestion13: ")
#13. Write a PYTHON program to reverse the given number
n12 = int(input("Enter the value of n: "))
rev = 0
while n12 > 0:
    digit = n12 % 10
    rev = rev * 10 + digit
    n12 = n12 // 10

print("Reverse number =", rev)







print("\nQuestion14: ")
#14. Write a PYTHON program to print the multiplication table
n13 = int(input("Enter the value of n: "))
i = 1
while i <= 10:
    print(n13, "x", i, "=", n13 * i)
    i = i + 1










print("\nQuestion15: ")
#15. Write a PYTHON program to print the largest of n numbers
n14 = int(input("Enter the number of elements: "))
i = 1
num = int(input("Enter number 1: "))
largest = num

while i < n14:
    num = int(input("Enter number " + str(i + 1) + ": "))
    if num > largest:
        largest = num
    i = i + 1

print("Largest number =", largest)










print("\nQuestion16: ")
#16. Write a PYTHON program to print smallest of n numbers
n15 = int(input("Enter the number of elements: "))
i = 1
num = int(input("Enter number 1: "))
smallest = num

while i < n15:
    num = int(input("Enter number " + str(i + 1) + ": "))
    if num < smallest:
        smallest = num
    i = i + 1

print("Smallest number =", smallest)
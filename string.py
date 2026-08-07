#Programs of STRING



print("\nQuestion1: ")
#1. Write a PYTHON program to input a string and display its length without using len() function
s = input("Enter a string: ")
count = 0
for ch in s:
    count = count + 1
print("Length of string =", count)





print("\nQuestion2: ")
#2. Write a PYTHON program to count vowels, consonants, digits, spaces and special characters
s = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0
for ch in s:
    if ch in "AEIOUaeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)







print("\nQuestion3: ")
#3. Write a PYTHON program to reverse the given string without using built-in reverse functions
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reverse string =", rev)







print("\nQuestion4: ")
#4. Write a PYTHON program to check whether the entered string is palindrome or not
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("String is Palindrome")
else:
    print("String is Not Palindrome")






print("\nQuestion5: ")
#5. Write a PYTHON program to count uppercase and lowercase letters in a string
s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
print("Uppercase letters =", upper)
print("Lowercase letters =", lower)









print("\nQuestion6: ")
#6. Write a PYTHON program to replace all occurrences of a given character with another character
s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in s:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("New string =", result)







print("\nQuestion7: ")
#7. Write a PYTHON program to remove all spaces from input string
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result = result + ch
print("String after removing spaces =", result)







print("\nQuestion8: ")
#8. Write a PYTHON program to find the number of times a specified character appears in a string
s = input("Enter a string: ")
ch = input("Enter character to find: ")
count = 0
for i in s:
    if i == ch:
        count = count + 1
print("Frequency of character =", count)







print("\nQuestion9: ")
#9. Write a PYTHON program to print the first and last character of a string
s = input("Enter a string: ")
print("First character =", s[0])
print("Last character =", s[-1])







print("\nQuestion10: ")
#10. Write a PYTHON program to display each character of a string along with its ASCII value
s = input("Enter a string: ")
for ch in s:
    print(ch, "=", ord(ch))







print("\nQuestion11: ")
#11. Write a PYTHON program to count the total number of words in a sentence
s = input("Enter a sentence: ")
count = 1
for ch in s:
    if ch == " ":
        count = count + 1
print("Total number of words =", count)







print("\nQuestion12: ")
#12. Write a PYTHON program to find the longest word in a given sentence
s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word =", longest)






print("\nQuestion13: ")
#13. Write a PYTHON program to find the shortest word in a sentence
s = input("Enter a sentence: ")
words = s.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word =", shortest)









print("\nQuestion14: ")
#14. Write a PYTHON program to convert first letter of every word to uppercase
s = input("Enter a sentence: ")
result = s.title()
print("Title Case =", result)






print("\nQuestion15: ")
#15. Write a PYTHON program to print all duplicate characters in a string
s = input("Enter a string: ")
duplicate = ""
for ch in s:
    if s.count(ch) > 1 and ch not in duplicate:
        duplicate = duplicate + ch
print("Duplicate characters are:", duplicate)









print("\nQuestion16: ")
#16. Write a PYTHON program to display the frequency of every character in a string
s = input("Enter a string: ")
visited = ""
for ch in s:
    if ch not in visited:
        print(ch, "=", s.count(ch))
        visited = visited + ch







print("\nQuestion17: ")
#17. Write a PYTHON program to check whether two strings are anagrams or not
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Strings are Anagram")
else:
    print("Strings are Not Anagram")







print("\nQuestion18: ")
#18. Write a PYTHON program to remove duplicate characters while maintaining original order
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result = result + ch
print("String after removing duplicates =", result)









print("\nQuestion19: ")
#19. Write a PYTHON program to check whether a given substring exists in main string
s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring exists")
else:
    print("Substring does not exist")








print("\nQuestion20: ")
#20. Write a PYTHON program to count how many times a specific word appears in a sentence
s = input("Enter a sentence: ")
word = input("Enter word to search: ")
words = s.split()
count = 0
for i in words:
    if i == word:
        count = count + 1
print("Occurrence of word =", count)








print("\nQuestion21: ")
#21. Write a PYTHON program to validate a password
password = input("Enter password: ")
upper = 0
lower = 0
digit = 0
special = 0
for ch in password:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1
    elif ch.isdigit():
        digit = digit + 1
    else:
        special = special + 1
if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Valid Password")
else:
    print("Invalid Password")










print("\nQuestion22: ")
#22. Write a PYTHON program to perform Run-Length Encoding
s = input("Enter a string: ")
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1
result = result + s[-1] + str(count)
print("Compressed string =", result)









print("\nQuestion23: ")
#23. Write a PYTHON program to compress repeated characters and return original if compression is not reduced
s = input("Enter a string: ")
result = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count = count + 1
    else:
        result = result + s[i] + str(count)
        count = 1

result = result + s[-1] + str(count)

if len(result) < len(s):
    print("Compressed string =", result)
else:
    print("Original string =", s)









print("\nQuestion24: ")
#24. Write a PYTHON program to find the character with highest frequency

s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most frequent character =", max_char)











print("\nQuestion25: ")
#25. Write a PYTHON program to find the second most frequent character

s = input("Enter a string: ")

characters = []

for ch in s:
    if ch not in characters:
        characters.append(ch)

first = 0
second = 0
second_char = ""

for ch in characters:
    count = s.count(ch)

    if count > first:
        second = first
        first = count
    elif count > second:
        second = count
        second_char = ch

print("Second most frequent character =", second_char)











print("\nQuestion26: ")
#26. Write a PYTHON program to implement Caesar Cipher

s = input("Enter a string: ")

shift = int(input("Enter shift value: "))

result = ""

for ch in s:
    if ch.isalpha():
        result = result + chr(ord(ch) + shift)
    else:
        result = result + ch

print("Encrypted string =", result)










print("\nQuestion27: ")
#27. Write a PYTHON program to validate email address

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")








print("\nQuestion28: ")
#28. Write a PYTHON program to count frequency of every word in a paragraph

s = input("Enter paragraph: ")

words = s.split()

visited = ""

for word in words:
    if word not in visited:
        print(word, "=", words.count(word))
        visited = visited + word + " "












print("\nQuestion29: ")
#29. Write a PYTHON program to reverse the order of words in a sentence

s = input("Enter sentence: ")

words = s.split()

rev = ""

for word in words:
    rev = word + " " + rev

print("Reversed sentence =", rev)















print("\nQuestion30: ")
#30. Write a PYTHON program to check whether one string is rotation of another

s1 = input("Enter first string: ")

s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, strings are rotation")
else:
    print("No, strings are not rotation")
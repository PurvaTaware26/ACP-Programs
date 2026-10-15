import re

print("Question 1:")
# Write a Python program using regular expressions to extract all digits from a given string.
text = "My roll number is 83 and marks are 95."
digits = re.findall(r'\d', text)
print("Digits:", digits)


print("\nQuestion 2:")
# Accept a sentence and display all words beginning with the letter A or a.
sentence = input("Enter a sentence: ")
words = re.findall(r'\b[Aa]\w*', sentence)
print("Words starting with A or a:", words)


print("\nQuestion 3:")
# Write a program to count the occurrences of vowels in a given string using regular expressions.
text = input("Enter a string: ")
vowels = re.findall(r'[aeiouAEIOU]', text)
print("Vowel count:", len(vowels))


print("\nQuestion 4:")
# Write a program to extract all uppercase letters from a given string.
text = input("Enter a string: ")
uppercase = re.findall(r'[A-Z]', text)
print("Uppercase letters:", uppercase)


print("\nQuestion 5:")
# Write a program to identify all spaces, tabs, and newline characters in a text.
text = "Hello World\tPython\nProgramming"
characters = re.findall(r'[ \t\n]', text)
print("Spaces, tabs and newlines:", characters)


print("\nQuestion 6:")
# Write a program to replace multiple consecutive spaces with a single space.
text = input("Enter a sentence: ")
result = re.sub(r' {2,}', ' ', text)
print("Result:", result)


print("\nQuestion 7:")
# Accept a sentence and display all words containing exactly five characters.
sentence = input("Enter a sentence: ")
words = re.findall(r'\b[A-Za-z]{5}\b', sentence)
print("Five-character words:", words)


print("\nQuestion 8:")
# Write a program to identify all words ending with the letter s.
sentence = input("Enter a sentence: ")
words = re.findall(r'\b\w+s\b', sentence, re.IGNORECASE)
print("Words ending with s:", words)


print("\nQuestion 9:")
# Write a program to remove all special characters while retaining letters, digits, and spaces.
text = input("Enter a string: ")
result = re.sub(r'[^A-Za-z0-9 ]', '', text)
print("Result:", result)


print("\nQuestion 10:")
# Write a program to count the number of words in a sentence using regular expressions.
sentence = input("Enter a sentence: ")
words = re.findall(r'\b\w+\b', sentence)
print("Word count:", len(words))


import re

print("Question 11:")

# Write a program to validate a 10-digit Indian mobile number.

mobile = input("Enter mobile number: ")

if re.fullmatch(r'[6-9]\d{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")


print("\nQuestion 12:")

# Accept an email address and check whether it follows a reasonable email format.

email = input("Enter email address: ")

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

if re.fullmatch(pattern, email):
    print("Valid email format")
else:
    print("Invalid email format")


print("\nQuestion 13:")

# Write a program to extract dates in DD-MM-YYYY format from a paragraph.

text = input("Enter a paragraph: ")
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print("Dates:", dates)


print("\nQuestion 14:")

# Write a program to identify web addresses beginning with http:// or https://.

text = input("Enter text containing URLs: ")
urls = re.findall(r'https?://[^\s]+', text)
print("URLs:", urls)


print("\nQuestion 15:")

# Write a program to extract all hashtags from a social media post.

text = input("Enter a social media post: ")
hashtags = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)
print("Hashtags:", hashtags)


print("\nQuestion 16:")

# Check whether a password has at least 8 characters, uppercase, lowercase, digit, and special character.

password = input("Enter password: ")

pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'

if re.fullmatch(pattern, password):
    print("Strong password")
else:
    print("Weak password")


print("\nQuestion 17:")

# Identify consecutive repeated words, ignoring case differences.

sentence = input("Enter a sentence: ")
words = re.findall(r'\b(\w+)\s+\1\b', sentence, re.IGNORECASE)
print("Repeated words:", words)


print("\nQuestion 18:")

# Extract six-digit Indian PIN codes from a paragraph.

text = input("Enter a paragraph: ")
pin_codes = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text)
print("PIN codes:", pin_codes)


print("\nQuestion 19:")

# Check whether an input matches a common Indian vehicle registration format, such as MH12AB1234.

number = input("Enter vehicle registration number: ").upper()

pattern = r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}'

if re.fullmatch(pattern, number):
    print("Valid registration format")
else:
    print("Invalid registration format")


print("\nQuestion 20:")

# Extract file extensions from filenames in a given string.

text = input("Enter filenames: ")
extensions = re.findall(r'\b[\w-]+\.([A-Za-z0-9]+)\b', text)
print("File extensions:", extensions)


import re

print("Question 21:")

# Remove HTML tags, extra whitespace, and unwanted punctuation from text.

text = "<p>Hello,   World!!! Welcome to <b>Python</b>.</p>"

text = re.sub(r'<[^>]+>', '', text)
text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r'\s+', ' ', text).strip()

print("Cleaned text:", text)


print("\nQuestion 22:")

# Extract invoice numbers, dates, and monetary amounts from invoice text.

text = """
Invoice No: INV-12345
Date: 15-10-2026
Amount: Rs. 2500.50
"""

invoice = re.findall(r'INV-\d+', text)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
amounts = re.findall(r'(?:Rs\.?|INR|₹)\s*[\d,]+(?:\.\d{2})?', text)

print("Invoice numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)


print("\nQuestion 23:")

# Identify single-line comments in Python source code.
# Regex alone may incorrectly identify # inside strings and cannot fully parse Python syntax.

code = """
# This is a comment
print("Hello")
# Another comment
x = 10  # Inline comment
"""

comments = re.findall(r'^[ \t]*#.*$', code, re.MULTILINE)
print("Comment lines:")
for comment in comments:
    print(comment)

print("Note: Regex alone cannot reliably distinguish comments from # inside strings.")


print("\nQuestion 24:")

# Validate product codes following the pattern ABC-1234-XY.

code = input("Enter product code: ")

pattern = r'[A-Z]{3}-\d{4}-[A-Z]{2}'

if re.fullmatch(pattern, code):
    print("Valid product code")
else:
    print("Invalid product code")


print("\nQuestion 25:")

# Extract student names, roll numbers, and marks from a paragraph.

text = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
"""

pattern = r'Name:\s*([A-Za-z ]+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'

students = re.findall(pattern, text)

for name, roll, marks in students:
    print("Name:", name.strip())
    print("Roll Number:", roll)
    print("Marks:", marks)


print("\nQuestion 26:")

# Extract DOI identifiers, publication years, email addresses, and URLs from research references.

text = """
Research Paper (2024). DOI: 10.1234/abcd.5678
Contact: author@example.com
Website: https://example.com/paper
Another paper (2022). DOI: 10.5678/xyz.1234
"""

dois = re.findall(r'\b10\.\d{4,9}/[^\s;,]+', text)
years = re.findall(r'\b(?:19|20)\d{2}\b', text)
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
urls = re.findall(r'https?://[^\s]+', text)

print("DOIs:", dois)
print("Publication years:", years)
print("Email addresses:", emails)
print("URLs:", urls)
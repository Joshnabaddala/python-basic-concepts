#1.Arithmetic Operations in Python:

# Addition
result = 5 + 3
print(result)  # Output: 8

# Subtraction
result = 10 - 2
print(result)  # Output: 8

# Multiplication
result = 4 * 6
print(result)  # Output: 24

# Normal Division
result = 15 / 3
print(result)  # Output: 5.0

# Floor Division
result = 4 // 2
print(result)

# Modular Division
result = 6 % 2
print(result)


#2.String Manipulation:

# Concatenation
first_name = "Joshna"
last_name = "Baddala"
full_name = first_name + " " + last_name
print(full_name)  

# Slicing
sentence = "Python program is easy to learn!"
print(sentence[0:6])  

# Formatting
age = 21
message = f"My age is {age}."
print(message) 

# 3. Conditional Statements:

# i. if condition
a=200
if a>100:
    print(a)

# ii. if-else condition
a=20
if a % 2 == 0:
    print(a,'is a even number')
else:
    print(a,'is a odd number')

# iii. if-elif condition
a=20
b=30
if a == b:
    print(a,b,'are equal')
elif a > b:
    print(a,'is maximum than',b)
else:
    print(b,'is maximum than',a)

# iv. nested-if condition
a=10
b=20
c=30
if a > b:
    if a > c:
        print('a is max')
    else:
        print('c is max')
else:
    if b > c:
        print('b is max')
    else:
        print('c is max')  


# 4.Common Data Structures:

# Lists
fruits = ["apple", "banana", "mango"]
print(fruits[1])  

# Dictionaries
person = {"name": "Joshna", "age": 21}
print(person["age"])  # Output: 25

# Tuples
coordinates = (10, 20)
print(coordinates[0])  # Output: 10

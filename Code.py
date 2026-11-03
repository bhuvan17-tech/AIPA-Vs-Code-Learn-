'''print("Hello")
print("="*20)
print("Welcome to Python")
print("="*20)
print((10+5)*5)
print("^"*20)
print("Welcome new code Emojy")
print("-"*20)
First_name = "Bhuvan"
Last_name = "Kumar"
Full_Name = "Bhuvan kumar"
Country = "India"
City = "Dehradun"
print(First_name)
print(Last_name)
print(Full_Name)
print(Country)
print(City)
print("My name is Bhuvan And I Don't have Enough python Knowledge",end=", ")
print("Currently I am learning python")
print("Also I am attend the clsses to learn Python")
#12First_Name = 
# !First_Name =
First_name_123 = "Vansh Kumar","1"
print(First_name_123)
a = "A"
print(ord(a))
num_one = 34
num_two = 35
Total = (num_two+num_one)
print(Total)                          #Total of num_one and num_two
Diff = (num_two-num_one)              #Subtract value by num_two from num_one
print(Diff)
Product = (num_two*num_one)           #Multiply the num_two*num_one
print(Product)
Division = (num_one/num_two)          #Division by the num_one/num_two
print(Division)
Reminder = (num_one%num_two)          #reminder num_one % num_two
print(Reminder)
floor_division = (num_one//num_two)   #Floor division of num_one and num_two use this (//)
print(floor_division)
pi = 3.14
radius = 30
Area_of_circle = (pi*radius**radius)  #Calculate the area of circle (pi*r^2)
print(Area_of_circle)
Circum_of_circle = (2*pi*radius)      #Calculate the circumference of a circle (2*pi*r)
print(Circum_of_circle)
Number_of_members = float(input("Write the number of members: "))         # User Input Function
print("The number of Members is: ",Number_of_members)
Salary_declare_for_Team_A = float(input("Write the value of Salary_declare_for_Team_A: "))                      # Change to data type its called "Type Converter" 
Salary_declare_for_Team_B = float(input("Write the value of Salary_declare_for_Team_B: "))
Total = Salary_declare_for_Team_A + Salary_declare_for_Team_B                                               # Agar aise hi terminal me output "str" me aayega.
print("Total salary- ",Total)          #iske "int" result ke liye user ko num_one ki value rakhte smay int() function ka use krna hoga.
a = int(69.69)
print(type(a))'''
'''num_one = int(input("Wrte a value: "))
num_two = 69
Total = num_one + num_two
print("Type of this value is: ", str(type(Total)) + "This is the answer: ",Total)'''
'''a = 1 
b = 1                    # (=) Single equal to for assign operator (==) Double equal to known as comparision
print(a == b)            # (==) (is) sign for check the value is the same or not either given same result 'True' Result is not same given 'False'
a = 2
b = 2
print(a != b)            # (!=) (is not) This sign for (is not) equal so basically this sign work for if answer is not equal given the result in 'True' if answer is equal given 'False'
a = 10 
b = 11
print(a > b)             # (>) This check for given b value a variable se greater h to 'True' variable se greater nhi h to 'False'
a = 7
b = 11
print(a >= b)            # (>=) This sign for given b variabel a variable se greater ya equal h to 'True' nhi to 'False'
a = 9
b = 11
print(a < b)             # (<)  This sign for given b variabel a variable se less h to 'True' nhi 'False
a = 3
b = 11
print(a <= b)            # (<=) This sign for given b variabel a variable se less or equal h to 'True' nhi to 'False'''
'''print(ord(" "))'''
'''a = 10 
print(a > 5 or ((a > 11 and a == 20)and a >= 10))'''
'''
and = &
or = | |
not = !
'''
'''   # f-strings
name = "Example Chandu champion"
age = 100
print("My name is ", name," and my age is ", age)
#* My name is Example chandu champion
#! f strings
print(f"My name is {name} and my age is {age}")
'''
'''   # Operator
name = "Example Chandu champion"                    # (%s) = "str"  (%d) = "int"  (%f) = "float"
age = 100
print("My Name is %s and my age is %d" %(name,age))
'''
'''
name = "Example Chandu champion"
age = 100
'''
'''
item = input("Enter item name: ")              #Ask for an item name, quantity, and price per item. Calculate the total cost and display a formatted bill line.
quantity = int(input("Enter quantity: ")) 
price = float(input("Enter price per item: ")) 
total = quantity * price 
print(f"{item}: {quantity} x {price:.2f} = {total:.2f}") 
'''
'''
word = input(" How are you: ") 

letter = input("What are you doing: ") 

if letter in word: 

    print("The letter occurs in the word.") 

else: 

    print("The letter does not occur in the word.")
'''
'''color1, color2, color3 = "Red", "Green", "Blue" 

print("Before swap:", color1, color2, color3)     # Swap first and third without a temporary variable 
color1, color3 = color3, color1 
print("After swap:", color1, color2, color3) '''
'''
total_seconds = int(input("Enter total number of seconds: ")) 
minutes = total_seconds // 60 
seconds = total_seconds % 60 

print(f"{minutes} minutes and {seconds} seconds")
'''
'''
name = input("Enter student's name: ") 
score1 = int(input("Enter first score: ")) 
score2 = int(input("Enter second score: ")) 
score3 = int(input("Enter third score: ")) 
average = (score1 + score2 + score3) / 3 
average_at_least_50 = average >= 50 
all_scores_at_least_40 = score1 >= 40 and score2 >= 40 and score3 >= 40 
print(f"Student: {name}") 
print(f"Average: {average:.2f}") 
print(f"Average at least 50: {average_at_least_50}") 
print(f"All scores at least 40: {all_scores_at_least_40}")
'''
'''
product_name = "Apple" 
unit_price = 50.0 
quantity = 3 
total = unit_price * quantity 
contains_a = 'a' in product_name.lower() 
quantity_not_zero = quantity != 0 
print(f"Product name contains 'a': {contains_a}") 
print(f"Quantity is not zero: {quantity_not_zero}") 
print(f"Purchase Summary: {product_name} x {quantity} @ ₹{unit_price:.2f} = ₹{total:.2f}") 
student_score = 140
print(student_score)
'''
'''def add(a, b):
    return a + b

print(add(4, 6))'''
'''
print("GYM Schedule o_o")
Day = input("What Day is it Today ? :")
if Day == " Monday" :
    print("Today is : Chest Day")
elif Day == " Tuesday" :
    print("Today is : Shoulder Day")    
elif Day == " Wednesday" :
    print("Today is : Biceps Day")
elif Day == " Thursday" :
    print("Today is : Abs Day")
elif Day == " Friday" :
    print("Today is : Back Day")
elif Day == " Saturday" :
    print("Today is : Legs Day")
elif Day == " Sunday" :
    print("Today is : Rest Day")
'''
'''
Client = int(input("Here you type Numbers :"))
if Client > 0 :
    print("The number is : Positive")
elif Client < 0 :
    print("The number is : Negative")
else:
    print("The number is : Zero")

num_1 = int(float(input("Enter numbers 1 : ")))
num_2 = int(float(input("Enter numbers 2 : ")))
Operation = int(input("1. sum, 2. sub, 3. multi, 4. div :- "))
if Operation ==  1 :
    print("The answer is : ", num_1 + num_2)
elif Operation == 2 :
    print("The answer is : ", num_1-num_2)
elif Operation == 3 :
    print("The answer is : ", num_1*num_2)
elif Operation == 4 :
    print("The answer is : ", num_1/num_2)
'''
'''
print("If the sum is under 10 to 20. It will be 'Between' otherwise, It will be 'Different'. ")
Num_one = int(input("Enter numbers 1 : ")) 
Num_two = int(input("Enter numbers 2 : "))
Result = Num_one + Num_two 
if 10 <= Result <= 20 :
    print("The answer is : Between")
else:
    print("The answer is : Different" )
'''
"""
print("Temprature Convertor Fahrenheit to Celsius ")
Fahrenheit = float(input("Enter the Farhenheit Degree : "))                #C =((5*F)/9)-32  (X)  Fahrenheit to Celsius  5/9*(Farhenheit-32) 
C = 5/9*(Fahrenheit-32)
print("The celsius degree is : ",C,"C")

print("Temprature Convertor Celsius to Fahrenheit ")
Celsius = float(input( "Enter the Celsius Degree : "))
F = 9/5*Celsius+32                                                         # F = 9/5*Celsius+32 (Celsius to Fahrenheit )
print("The Fahrenheit degree is : ",F,"F")
"""


'''
Client_1 = float(input("Enter the value number one : "))
Client_2 = float(input("Enter the value number two : "))
if Client_1 > Client_2 : 
    print("The value number one is bigger than value number two : ")
elif Client_2 > Client_1 :
    print("The value number two is bigger than value number one : ")
else :
    print("Both values are equal. ")
'''
"""
Client_1 = float(input("Enter the value number one : "))
Client_2 = float(input("Enter the value number two : "))
Client_3 = float(input("Enter the value number three : "))
if Client_1 > Client_2 and Client_1 > Client_3 : 
    print("The value number one is bigger than value number two and three : ")
elif Client_2 > Client_1 and Client_2 > Client_3 :
    print("The value number two is bigger than value number one and three : ")
elif Client_3 > Client_1 and Client_3 > Client_2 :
    print("The value number three is bigger than value number one and two : ")
elif Client_1 == Client_2 == Client_3 :
    print("All values are equal. ")
"""
'''
Client_1 = int(input("Enter the numbers : "))
if Client_1 % 2 == 0 and Client_1 % 5 == 0 :
    print("Divisible by both 2 and 5. ")
elif Client_1 % 2 == 0 :
    print("Divisible by 2. ")
elif Client_1 % 5 == 0 :
    print("Divisible by 5. ")
else :
    print("ot divisible by Either. ")
'''
"""
Client_1 = float(input("Enter the value number one : "))
Client_2 = float(input("Enter the value number two : "))
Client_3 = float(input("Enter the value number three : "))
if Client_1 > Client_2 :
    if Client_1 > Client_3 :
        print("The value number one is bigger than value number two and three : ")
    else:
        print("The value number three is bigger than value number one and two : ")
elif Client_2 > Client_1 :
    if Client_2 > Client_3 :
        print("The value number two is bigger than value number one and three : ")
    else:
        print("The value number three is bigger than value number one and two : ")
else : 
    print("All values are the same. ")
"""
"""
Number_one = int(input("Enter the numbers here : "))
if Number_one % 2 == 0 :
    print("The number is Even. ")
elif Number_one % 2 != 0 :
    print("The number is Odd. ")
"""
"""
for i in range(1,101,2):
    print(i)
"""
"""
for i in reversed(range(1,100)) :
    if i % 2 != 0 :
        print(i,end=" ")
"""
'''
for i in range(1,11):
    # print("5 X", i, "=", 5*i)
    print(f"5 X {i} = {5*i}")
'''
'''
for i in range(1,11):
    print(f"69 X {i} = {69*i}")

print("Hello", "Python", sep="-")
'''
'''
temperature = 15 
if temperature > 25: 
    print("Hot") 
elif temperature >= 15: 
    print("Cool") 
else: 
    print("Cold") 
'''
'''
colors = ["red", "blue"] 
for color in colors: 
    print(color) 
'''
'''
n = int(input("Enter the positive number here : "))   
# total = 0 
for i in range(1,n+1):  
    # total += i 
    print(f"The total of the numbers from 1 through {n} is {i} ") 
'''
'''
for i in range(1,6):
    print()
    for j in range(i):
        print("*", end="")                      #for create triangle
'''
'''
for i in range(1,11):
    print()
    for j in range(1,i):
        print(j, end=" ")
'''
'''
for i in range(2):
    for j in range(2):
        for k in range(5):
            print(k, end="")

        print()
    print()
'''
'''
for i in (range(1,11)):
    print()
    for j in (range(i)):
        print(i, end=" ")
'''
'''
n = int(input("Enter the positive numbers here : "))                                    #mathematics formula:- n*(n+1)/2
print()
total = 0                                                                            #Python format:- total = 0, total +=i, /current value of total is 0, o+i, o+0= 0.
for i in range(1,n+1):                                                               #Python format:- total = 0, total +=i, /current value of total is 0, o+i, o+1= 1.
    total += i                                                                       #Python format:- total = 0, total +=i, /current value of total is 1, o+i, 1+2= 3. 
print(f"The total of the numbers from 1 through {n} is: {total} ")                   
'''
'''
n = int(input("Enter the positive numbers here : "))  
Total = n*(n+1)//2
print(f"The total of the numbers from 1 through {n} is: {Total} ")
'''
'''
print()
n = int(input("Enter the positive numbers here : "))   
total = 1
for i in range(1,n+1): 
    total *= i
print(f"The multiplication numbers from 1 through {n} is: {total} ")
print()
'''
'''
print()
total = 1 
for i in range(1,100):
    total *= i 
    print(f"The multiplication numbers from 1 through {i} is: {total} ")
# print(f"The multiplication numbers from 1 through  is: {total} ")
print()
'''
'''
n = 0
while n < 5:
    n += 1
    print(n)
'''
'''
i = 1
while i < 50:
    if i % 2 == 0:
        print(i)
    i += 1
'''
'''
i = 1
while i < 50:
    if i % 2 != 0:
        print(i)
    i += 1                                        # i = i + 1
'''
'''
for i in range(0, 51):                          # Print even numbers from 0 to 50 using a for loop
    # Check if the number is even
    if i % 2 == 0:
        print(i)
'''
"""
# This is the the while loop output project I made.
user = ""
while user.lower()!='quit':
    user = input("Enter something (type 'quit' to stop): ")
    print(f"You Entered : {user} ")
"""
'''
user = ""
count = 0
while user.lower()!='quit' and count < 5:
    print()
    user = input("Enter something (type 'quit' to stop): ")
    print(f"You Entered : {user} ")
    count += 1
print()
'''
'''
password = ""
count = 0 
while password != 'python123' and count < 3 :
    password = input("Enter password: ")
    count += 1
    
    if password == "python123":
        print("Access granted")
    else:
        print("Wrong Password ")
        
if password != "python123":
    print("Account locked")
'''
'''
user = ""
count = 0
while user.lower() != "yes" and count < 5:
    print()
    user = input("You can type (yes) : ")
    count += 1
    if user.lower() == "yes":
        print(end="\n")
        print("Correct ")
        print()
    else:
        print()
        print("Try again.")
if user.lower() != "yes":
    print("Attempt over !! ")
    print()
'''
'''
# Program to count positive, negative, and zero numbers from 10 inputs

# Initialize counters
positive_count = 0
negative_count = 0
zero_count = 0

print("Enter 10 numbers:")

for i in range(1, 11):
    try:
        num = float(input(f"Number {i}: "))  # Accept integers or decimals
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        exit(1)  # Exit if invalid input is given

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display results
print("\nResults:")
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")
'''
'''
Student = 'Aa'
Students = ["abc","bca","Aa","Bb"]
for Student in Students:
    if Student == 'Aa':
        continue
    print(Student)
'''
'''
count = 0 
while count < 10 :
    count += 1
    if count == 6:
        continue
    print(count)
'''
'''
count = 0
while count < 30 :
    count += 1
    if count % 3 == 0 :
        continue
    print(count)
'''
'''
count = 0
while count < 20 :
    count += 1
    if count > 10 and count % 4 == 0 :
        break
    print(count)
'''
'''
count = 0
while count < 15 :
    count += 1
    if count % 2 == 0:
        continue
    if count > 10 :
        break
    print(count)
# '''
"""
num = 5
while num <= 5 :
    if num > 5:
        num += 1
    print(num)
"""
"""
# List function in python
array = [1,2,3,4,'yes', 'no', 12,13]
print(array[5])                              #For take output

 particular value 
# array[4] = "Oh Yes"                          #For modify or replace value us with index
# array.append("Python")                       #For add new value in list also add value on last in list
# b = array.copy()                             #For copy first vaariable to another variable   
print(array)
"""
'''
fruits = ['apple', 'banana', 'mango']
fruits[1] = 'Kiwi'
fruits.append('orrange')
fruits.insert(0,'grape')
fruits.remove('mango')
print(fruits)
'''
'''
Items = ['books', 'pencil', 'eraser']
if 'pen' in Items :
    Items.remove('pen')
else:
    print("If did not run beacause it was not there")
print(Items)
'''
'''
total = 0 
for n in range(1, 8): 
    if n % 3 == 0: 
        continue 
    total += n 
print(total) 
'''
'''
n = 305 
digits = 0 
while n > 0: 
    n //= 10 
    digits += 1 
print(digits) 
'''
'''
marks = 80 
if marks >= 40 and marks < 75 : 
    print('Pass') 
elif marks >= 75: 
    print('Distinction')
'''
'''
fruits = ["apple", "banana", "cherry"] 

for fruit in fruits: 

    print(fruit)
'''
'''
total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")
'''
'''
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

total = num1 + num2

if 10 <= total <= 20:
    print(15)
else:
    print(0)
'''
'''
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ").upper()

if unit == "C":
    f = (temp * 9 / 5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f} F")
elif unit == "F":
    c = (temp - 32) * 5 / 9
    print(f"Temperature in Celsius: {c:.2f} C")
else:
    print("Invalid unit")
'''
'''
month = input("Enter the month name: ").lower()

if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
elif month == "february":
    print("28 or 29 days")
else:
    print("Invalid month")
'''
'''
marks = float(input("Enter marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")
'''
'''
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
'''
'''
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
'''
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

for i in range(num1 + 1, num2):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
'''
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

a, b = 0, 1

while a <= num2:
    if a >= num1:
        print(a)
    a, b = b, a + b
'''
'''
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
'''
'''
num = int(input("Enter an integer: "))

n = abs(num)
digit_sum = 0
reverse = 0

while n > 0:
    digit = n % 10
    digit_sum += digit
    reverse = reverse * 10 + digit
    n //= 10

print(f"Sum of digits: {digit_sum}")

if num < 0:
    reverse = -reverse

print(f"Reversed number: {reverse}")
'''
'''
Secret_number = 34
Attempts_counter = 0
while Attempts_counter < 7:
    guess = int(input("Enter your guess 0-50: "))
    Attempts_counter += 1

    if guess > Secret_number:
        print("To High")
    elif guess < Secret_number:
        print("To Low")
    elif guess == Secret_number:
        print("Correct ")
        break
else:
    print("Out of attempts")
'''
"""
# ATM Code
balance = 10000
pin = 4321
attempts = 0

while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Attempts left:", 3 - attempts)

if attempts == 3:
    print("Too many incorrect attempts. Account locked.")
else:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Current balance: Rs. {balance:.2f}")

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print(f"Deposit successful. Balance: Rs. {balance:.2f}")
            else:
                print("Invalid deposit amount.")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount % 100 != 0:
                print("Withdrawal must be a multiple of 100.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrawal successful. Balance: Rs. {balance:.2f}")

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")
"""
"""
# Student marks Average of Class
n = int(input("Enter the number of students: "))

total = 0
highest = -1
passed = 0

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Invalid marks!")
        continue
    elif marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: Grade {grade}")

    total += marks

    if marks > highest:
        highest = marks

    if marks >= 40:
        passed += 1

if n > 0:
    valid_students = n  # Assumes all marks entered are valid
    average = total / valid_students

    print(f"\nClass average: {average:.2f}")
    print(f"Highest mark: {highest}")
    print(f"Students scoring 40 or more: {passed}")
"""
"""
rows = 4

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
"""
"""
num = int(input("Enter an integer: ")) 

 

original = num 

total = 0 

reverse = 0 

 

while num > 0: 

    digit = num % 10 

    total = total + digit 

    reverse = reverse * 10 + digit 

    num = num // 10 

 

print("Sum of digits:", total) 

print("Reversed number:", reverse)
"""
'''
# for reverse output
a = "hello"
n = len(a) - 1
b = ""
while n >= 0:                                             # for while loop reverse output
    b += a[n]
    n -= 1
print(b)
'''
"""
ages = [19,22,19,24,20,25,26,24,25,24]
print(sorted(ages))                                        #for sorted 
print(ages[:: -1])                                         # for reversed 
min_age = min(ages)
max_age = max(ages)
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

ages.append(min_age)                                     # Value Add in list 
ages.append(max_age)
print(f"List after adding min and max: {ages}")
average_age = sum(ages) / len(ages)                  #Find average in list without using for loops
print(f'Average age: {average_age}')

age_range = max_age - min_age                         #Find Range of list
print(f"Range of the ages: {age_range}")
"""
'''
fruits = ['apple', 'mango', 'kiwi']
for i in range(len(fruits)) :
    print(fruits[i].upper())
'''
'''
ages = [19,22,19,24,20,25,26,24,25,24]
print(ages[:: -1])                          #for reverse list
'''
'''

ages = [19,22,19,24,20,25,26,24,25,24]
total = 0 
for i in ages:                            #Find average use with for loops
    total += i
print(total)
print("Average: ", total/len(ages))
'''

'''
# Dictionary function
person = {
    'first_name': "Example",
    'last_name': "Apple",
    'age': 18,
    'skills': ['Gaming', 'Sleeping'],
    'address':{
        'state': "up",
        'city':{
            'name' : "Baghpat"
        }
    },
    0:"Allright"
}

person['age'] = 24
person['skills'][1] = "Overthinking"
person['skills'].append("Sleeping")
print(person['skills'])
print(person[0])
print(person)
print(person.values())
print(person.keys())
print(person.items())                          # Convert dictionary to list 

for key in person:                             # Show output only key use with loop
    print(key)

for value in person.values():                  # Show output only key use with loop
    print(value)

for key , value in person.items():             # Sow both output key and value use with for loop
    print(key, ":", value)

person.popitem()                             # Delete last values
del person                                   # For delete variable and all values

# pop() if I want remove a particular key
# popitem() automatically removes last key
# del() remove everything 

'''
'''
dog = {
    'name': "Labro",
    'colour': "blackish-white",
    'bread': "Husky",
    'legs': 4,
    "age": 3
}

student = {
    "first_name": "John",
    'last_name': 'Doe',
    'gender': 'M',
    'age': 23,
    'marital_status': 'NA', 
    'skills': ['Python', 'Java', 'Django', 'C#'],
    'country': 'IND',
    'city': 'Mumbai',
    'address': 'Dharavi'
}

# print(len(student))
# print(type(student['skills']))
# student['skills'].append('SQL')
# print(student['skills'])
# print(student.keys())
# print(student.items())
# print(student.popitem())
# print(student.pop('age'))
# print(student)
# del student


# for import function use        
from Function import greet
print(greet())
'''
'''
# Polymorphism Duck Typing
class UPI:
    def pay(self, amount):
        print(f"{amount}₹ is paid via UPI ")

class Cash:
    def pay(self, amount):
        print(f"{amount}₹ is paid via Cash")

def checkout(method, amount):
    method.pay(amount)

checkout(UPI(), input("Enter the amount if you pay with UPI either type zero. "))
print()
checkout(Cash(), input("Enter the amount if you pay with Cash either type zero. "))
'''
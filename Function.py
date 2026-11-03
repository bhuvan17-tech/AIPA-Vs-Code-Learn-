'''
""" Function Basic code """
def Function_name():
    print('Example says I am learning')                               # Function Basic code

Function_name()
'''
'''
""" Function use according to function call """
def Function_name_2(name):
    print(f"{name } Says keep it up")                                # Function use name according to function call

Function_name_2('Solution')
'''
'''
""" Function use and take user input to call in output """
def Example(name):
    print("Today", name ,"Learn New codes in python")
    print("Today", name_1 ,"Don't lear new codes in python")
print()
name = input("Enter a name who learn code: ")
name_1 = input("Enter a name who don't learn code: ")

print()

Example(name)

print()
'''
'''
"""Create calculator for using of Function"""
def calculator():                                                             # Create calculator for using of Function
    num_1 = int(input("Enter first number: "))
    option = input("Enter + or - or * or /: ")
    num_2 = int(input("Enter second number: "))
    if option == "+":
        return num_1 + num_2
    elif option == "-":
        return num_1 - num_2
    elif option == "*":
        return num_1 *  num_2
    elif option == "/":
        return  num_2 / num_1


print(calculator())

'''
'''
def odd_even_checker(user_input):
    if user_input % 2 == 0:
        return f"The {user_input} number is Even. "
    else:
        return f"The {user_input} number is Odd. "

user_input = int(input("Enter a number: "))

print(odd_even_checker(user_input))

'''
'''
def data_type_checker(list):
    list = ['Hello', 1, 2, 3 ,3 , 'yes', 'no', 'yeah', 'ohh',] 
    if list == str:
        return f" List all items data type is same. "
    elif list == int:
        return f" List all items data type is same. "
    elif list == float:
        return f" List all items data type is same. "

print(data_type_checker(list))

'''
'''
def data_type_checker(list):
    first_type = type(list[0])
    for item in list:
        if first_type != type(item):
            return f" List all items data type are not same. "
        
        return f" List all items data types are same. "


print(data_type_checker(['Hello', 'yes', 1, 2, 3 ,3, 'no', 'yeah', 'ohh']))
'''
'''
def data_type_checker(list):
    return all(type(item)) == type(list[0]) for item in list

print(data_type_checker([1,2,3,4,5,'yes', 'no','BASIC']))
'''
'''
def greet():
    name = "Example"                  # from this to down
    return f"My name is {name}. "   

# from Function import greet
# print(greet())                      # for import function use        
'''
'''
def func1(*args):
    print("Printing values:")
    for value in args:
        print(value)

func1(20, 40, 60)
func1(80, 100)
'''
'''
def calculation(a, b):
    sum = a + b
    difference = a - b
    return sum, difference

result = calculation(40, 10)
print(result[0], result[1])
'''
'''
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)


show_employee("Ben", 12000)
show_employee("Jessa")
'''
'''
def outer_function(a, b):
    def inner_function():
        return a + b

    result = inner_function()
    result = result + 5

    return result

print(outer_function(5, 10))
'''
'''
def addition(num):
    if num == 0:
        return 0
    else:
        return num + addition(num - 1)

print(addition(10))
'''
'''
def display_student(name, age):
    print(name, age)

# Assign another name to the function
show_student = display_student

# Call the function using the new name
show_student("Emma", 26)
'''
'''
def even_numbers():
    return list(range(4, 30, 2))


print(even_numbers())
'''
'''
def largest_number(x):
    largest = x[0]

    for num in x:
        if num > largest:
            largest = num

    return largest

x = [4, 6, 8, 24, 12, 2]
print(largest_number(x))
'''
'''
def describe_pet(animal_type, pet_name):
    print("I have a", animal_type + ".")
    print("My", animal_type + "'s name is", pet_name + ".")


# Calling with positional arguments
describe_pet("hamster", "Harry")

# Calling with keyword arguments
describe_pet(animal_type="dog", pet_name="Willie")
'''
'''
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)


print_info(name="Alice", age=30, city="New York")
'''
'''
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" ")


print_info(name="Alice", age=30, city="New York")
'''
'''
global_var = 10

def modify_global():
    global global_var
    global_var = 20


print("Initial:", global_var)

modify_global()

print("Modified:", global_var)
'''
'''
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


number = 5
print("The factorial of", number, "is", factorial(number))
'''
'''
# Create a lambda function to calculate square
square = lambda number: number * number

# Given input
number = 5

# Print the result
print(square(number))
'''
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
'''
'''
numbers = [1, 2, 3, 4, 5]

# Double each number using lambda and map()
double_numbers = list(map(lambda x: x * 2, numbers))

print(double_numbers)
'''
'''
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]

# Sort students by grade (lowest to highest)
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
'''
'''
# Addition function
def add(a, b):
    return a + b

# Multiplication function
def multiply(a, b):
    return a * b

# Higher-order function
def apply_operation(func, x, y):
    return func(x, y)


# Calling apply_operation with addition
print("Addition Result:", apply_operation(add, 5, 3))

# Calling apply_operation with multiplication
print("Multiplication Result:", apply_operation(multiply, 5, 3))
'''
'''
# Web Request
import requests
web_url = "https://aimicrodegree.org/"
response = requests.get(web_url)
response.headers
print(response)
'''
'''
import requests
from bs4 import BeautifulSoup

def scrape_example ():
    url = "https://claude.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.get_text()
        print(f"Title of this page : {title}")

    else:
        print(f"Failed to retrieve the page. Status code : {response.status_code}")

if __name__ == "__main__":
    scrape_example()
'''
'''
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

h3 = (soup.find('h3'))
print(h3.a["title"])
'''
'''
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Claude_(AI)"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

section = (soup.find('h3', id= "Application_programming_interface"))
# div = (soup.find('div', class_ = 'mw-heading mw-heading3'))
print(section)
'''
'''
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div = (soup.find('div', class_= 'product_price'))
print(div.p.text)
'''
"""
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product price divs
divs = soup.find_all('div', class_='product_price')

# Loop through all books
for div in divs:
    print(div.p.text)
"""
'''
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

h3a = soup.find_all('h3')

for h3 in h3a:
    print(h3.a['title'])
'''

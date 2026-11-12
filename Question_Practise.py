'''
result = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 == 0:
        result.append(str(num))

print(",".join(result))
'''
"""
num = (input("Enter a number: "))
smallest = min(num)
largest = max(num)

print("Smallest number is: ", smallest)
print("Largest number is: ", largest)
"""
'''
num = input("Enter a number: ").strip()
smallest = num[0]
largest = num[0]

for i in num:
    if i.isdigit():
        i = (i)
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

print(f"Smallest number is: {smallest}")
print(f"Largest number is: {largest}")
'''
'''
num = input("Enter a number: ")
smallest = int(num[0])
largest = int(num[0])

for i in num:
    i = int(i)
    i = (i)
    if i < smallest:
        smallest = i
    if i > largest:
        largest = i

print(f"Smallest number is: {smallest}")
print(f"Largest number is: {largest}")
'''
'''
# For odd and even number checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The {num} number is Even. ")
else:
    print(f"The {num} number is Odd. ")
'''
'''
# For prime or not prime number checker
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"The {num} number is Prime. ")
else:
    print(f"The {num} number is Not Prime. ")
'''
'''
num = [1,2,3,4,5,6,7,8,9,10]
sum = sum(num)
print(f"The sum of the numbers in the list is: {sum}")
'''
'''
# For prime or not prime number checker from sir methods
class functions:
    def prime(self):
        self.num = int(input("Enter a number: "))
        count = 0
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                count += 1
        # return True if count == 2 else False
        if count == 2:
            print(f"The {self.num} number is Prime. ")  
        else:
            print(f"The {self.num} number is Not Prime. ")

object = functions()
object.prime()
'''

num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0 :
        count += 1
if count == 2:
    print(f"The {num} is prime. ")
else:
    print(f"The {num} is not prime. ")

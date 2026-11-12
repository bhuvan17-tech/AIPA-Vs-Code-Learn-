'''
result = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 == 0:
        result.append(str(num))

print(",".join(result))
'''

num = (input("Enter a number: "))
smallest = min(num)
largest = max(num)

print("Smallest number is: ", smallest)
print("Largest number is: ", largest)
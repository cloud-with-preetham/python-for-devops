env = input("Enter the Environment: ")  # Taking input from the user

print("The user input environment is:", env)

# Conditional statemnet simple if else

# == != > < >= <=
if env == "prod": # True or False
    print("Don't Deploy on Friday")
elif env == "staging": # True or False
    print("Take backup and proceed testing")
else: # False
    print("Safe to deploy any day...!")
"""
# Type Casting - conversion of 1 data type to another
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(type(a))


print("Addition is:", a + b)
print("Subraction is:", a - b)
print("Multiplication is:", a * b)
print("Division is:", a / b)
print("Percentage is:", a % b)
print("Floor Division is:", a // b)
print("Power of is:", a**b)
"""

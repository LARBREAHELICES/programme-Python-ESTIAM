"""
A simple program that computes the sum and average of two numbers.
"""

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compute the sum
total = num1 + num2
PRECISION = 2

# Compute the average
average = round( total / 2, PRECISION )

# Display the results
print("The sum of the two numbers is:", total)
print("The average of the two numbers is:", average)

""" 
A simple program that asks for the user's name and greets them.
"""

# Ask the user for their name
user_name = input("What is your name? ")

# Display a personalized message
print("Hello", user_name + "!")
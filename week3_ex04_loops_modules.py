# Question 1: Using a for loop with a list

fruits = ["apple", "banana", "orange", "mango"]

for fruit in fruits:
    print(fruit)


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

count = 5

while count > 0:
    print(count)
    count -= 1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

for i in range(1, 11):
    print(i * i)


#-------------------------------------------------------------------------
# Question 4: Using the random module

import random

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(3):
    print(random.choice(colors))


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# NOTE: You must create a separate file called math_operations.py

import math_operations

print("Add:", math_operations.add(5, 3))
print("Subtract:", math_operations.subtract(10, 4))
print("Multiply:", math_operations.multiply(6, 2))
print("Divide:", math_operations.divide(8, 2))


# Simple calculator using while loop

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    if operation == "q":
        break

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")
# Question 1: Arithmetic and Assignment Operators

x = 10
y = 5

# Add 3 to x
x += 3

# Multiply y by 2
y *= 2

# Divide x by y
result = x / y

print("Result:", result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

a = 8
b = 4
c = 6

cond1 = a > b
cond2 = b % 2 == 0
cond3 = c <= a

final_condition = cond1 or (cond2 and cond3)

print("Final condition:", final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

score = int(input("Enter your test score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation"

print("Result:", result)
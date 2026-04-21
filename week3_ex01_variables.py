# Question 1: Variable Assignment and String Manipulation

# Ask user for name
name = input("Enter your name: ")

# Ask user for age
age = input("Enter your age: ")

# Print greeting
print("Hello " + name + ", you are " + age + " years old!")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# Ask for length
length = int(input("Enter the length of the rectangle: "))

# Ask for width
width = int(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Print result
print("The area of the rectangle is:", area)

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# Ask for temperature
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print result rounded to 2 decimals
print("Temperature in Fahrenheit:", round(fahrenheit, 2))
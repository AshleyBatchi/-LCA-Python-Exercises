# Question 1: Basic Function Definition and Calling

# Define function
def greet():
    print("Hello, World!")

# Call function
greet()


#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# Define function
def personalized_greeting(name):
    print("Hello, " + name + "!")

# Call function with your name
personalized_greeting("Ashley Batchi")


#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# Define function
def square(number):
    return number * number

# Call function and print result
print("Square of 5:", square(5))


#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# Define function
def rectangle_area(length, width):
    return length * width

# Call function and print result
print("Rectangle area:", rectangle_area(4, 5))


#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# Define function
def apply_operation(func, number):
    return func(number)

# Define function
def double(number):
    return number * 2

# Use apply_operation with double
print("Double of 7:", apply_operation(double, 7))

# Use apply_operation with square
print("Square of 3:", apply_operation(square, 3))
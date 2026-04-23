# Question 1: Creating and Modifying Lists

fruits = ["apple", "banana", "orange"]

# Add a fruit to the end
fruits.append("mango")

# Insert a fruit at the beginning
fruits.insert(0, "grape")

# Remove a fruit
fruits.remove("banana")

# Print modified list
print("Fruits:", fruits)


#-------------------------------------------------------------------------
# Question 2: List Operations

numbers = [1, 2, 3, 4, 5]

# Squared list
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

# Sum and average
total = sum(numbers)
average = total / len(numbers)

print("Squared numbers:", squared_numbers)
print("Sum:", total)
print("Average:", average)


#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

countries = {
    "South Africa": "Pretoria",
    "USA": "Washington D.C",
    "France": "Paris"
}

# Add new pair
countries["Japan"] = "Tokyo"

# Update existing
countries["USA"] = "Washington"

# Remove a pair
del countries["France"]

print("Countries:", countries)


#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

# Print keys
print("Fruits:", fruit_colors.keys())

# Print values
print("Colors:", fruit_colors.values())

# Print key-value pairs
for fruit, color in fruit_colors.items():
    print(fruit, "is", color)

# Check if fruit exists
fruit_check = "apple"

if fruit_check in fruit_colors:
    print(fruit_check, "color is", fruit_colors[fruit_check])
else:
    print("Fruit not found")
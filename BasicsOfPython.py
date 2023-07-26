## Beginning the Python Demonstration 

# This comment will not be executed. 
# The next line is a integer variable assignment. 
x = 5 

# Python uses indentation to indicate a block of code. 
# Here is a simple for loop to demonstrate this. 
for i in range(x):
    # this is insde the for loop and indented. 
    squared_value = i ** 2 # squarring the current x value 

    # printing the squared value of x. 
    print(f"Square of {i} is {squared_value}")

# Variables in Python are dynamically typed. 
# Unlike Java, you can assign any type to a variable without declaring its type. 
x = "15 and smoothie" # Now x is a string and not an integer! 

# Displaying the x value after reassigning. 
print (x)

# Here is the demonstration of a conditional logic. 
if x == 5: 
    print("x is 5.")
else:
    print(f"x is {x}, not 5.") # this will be executed since x is not 5. 


## Python Data Types Demonstration

# --- Numbers --- 

# Integers 
int_num = 10 
print(f"Integer: {int_num}")

# Floating-point numbers
float_num = 10.5 
print(f"Float: {float_num}")

# Complex numbers
complex_num = 9 + 3j
print(f"Complex: {complex_num}")

# Arithmetic operation
result = int_num + float_num
print(f"Sum of {int_num} and {float_num} is: {result}")


# --- Strings --- 

# Using single quotes
single_quote_string = 'Hello Python!'
print(single_quote_string)

# Using double quotes
double_quote_string = "Hello Python!"
print(double_quote_string)

# Multi-line strings with triple quotes 
triple_quote_strings = """Hello, 
Python 
3.11"""
print(triple_quote_strings)

# String concatenation
combined_string = single_quote_string + " " + double_quote_string
print(combined_string)


# --- Booleans ---

python_is_fun = True
print(f"Is Python fun? {python_is_fun}")

# Boolean operation 
is_even = int_num % 2 == 0
print(f"Is {int_num} an even number? {is_even}")


# --- Lists ---

list_data = [1,2,3,4,5]

# Adding element to the list 
list_data.append(6) # to the end of list
print(f"List after appending: {list_data}")
list_data.insert(3, 3) # insert 3 at index 3 
print(f"List after appending and inserting: {list_data}")


# --- Tuples --- 

tuple_data = (10, 20, 30)
print(f"Tuple: {tuple_data}")

# Accesing to tuple element
print(f"Second element of tuple data: {tuple_data[1]}")


# --- Dictioneries --- 

dict_data = {"name": "John", "age": 32, "city": "Austin"}
print(f"Dictionary: {dict_data}")

# Accessing dictionary value by key
print(f"Name from dictionary: {dict_data['name']}")


# --- Sets ---

set_data = {1,2,3, 4, 4, 5}
print(f"Set (duplicates removed): {set_data}")

# Adding to a set 
set_data.add(6)
print(f"Set after adding 6: {set_data}")

print("End of Data Type Demonstration!")


## Control Structures in Python

# --- If-Else Statements ---

num = 10

# Check if the number is greaterhn than 5. equal to 5, or less than 5
if num > 5: 
    print(f"{num} is greater than 5.")
elif num == 5:
    print(f"{num} is equal to 5.")
else:
    print(f"{num} is less than 5.")


# --- For Loop ---

# List of fruits 
fruits = ['apple', 'kiwi', 'cherry']
# Print each fruit in the list
print("\nFruits in the list")
for fruit in fruits:
    print(fruit)


# --- While Loop --- 

# Initialize a countdown number
count = 3 

# Perform a countdown using a while loop 
print("\nCountdown using while loop:")
while count > 0:
    print(count)
    count -= 1


# --- Using range() with For Loop ---

# Print numbers from 5 to 9
print("\nUsing range in for loop:")
for i in range(5, 10):
    print(i)


# --- Break & Continue ---

# Looping numbers and demonstrating 'break' and 'continue' statements 
print("\nUsing break and continue:")
for num in range(10):
    # Skip the iteration when num is 3 
    if num == 3:
        continue
    # Stop the iteration when num is 7
    if num == 7:
        break
    print(num)


# --- Iterating over Strings ---

string_data = "Python"

# Print each character in the string 
print("\nIterating over string:")
for char in string_data:
    print(char)


# --- Try-Except Blocks ---

# Handle exceptions using try-except
print("\nHandling erros usinf try-except:")

# Attempt division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed!")

# Attempt to convert a non-numeric string to an integer
try:
    int("B")
except ValueError:
    print("Converting letter to integer caused a ValueError!")


# --- For Loop with Else ---
print("\nFor loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished.")

# End of control structure demonstration message
print("\nEnd of Control Structures Demonstration!")


## Functions in Python 

# --- Defining Functions --- 

# Define a simple function to great a user 
def greet(name):
    return f"Hello, {name}!"

# Function to calculate the square of a number 
def square(num):
    return num * num 

# Define a function that accepts multiple arguments 
def add_numbers(a, b, c):
    return a + b + c

# Define a function with default arguments 
def power(base, exponent=2):
    return base ** exponent


# --- Callinf Functions --- 

# Call the greet function
user_name = "Ada"
print(greet(user_name))

# Call the square function
number = 4 
print(square(number))

# Call add_numbers function 
print(f"Sum of 1, 2 and 3 is: {add_numbers(1,2,3)}")

# Call power function with or without exponent
print(f"3 raised to the power 2 is: {power(3)}")
print(f"2 raised to the power 4 is: {power(2,4)}")


# --- Arguments --- 

# Positional arguments 
print(greet("Emma"))
      
# Keyword arguments 
print(add_numbers(b=2, a=1, c=3))

# Mixing positional and keyword arguments 
print(power(3, exponent=3))


# --- Lambda Functions ---

# Define a lambda function to double a number 
double = lambda x: x * 2

# Define a lambda function to add two numbers 
add = lambda x, y: x + y 

# Call the lambda functions 
print(f"Double of 5 is: {double(5)}")
print(f"Sum of 3 and 4 using lambda is: {add(3, 4)}")

# Using lambda with a higher order function 'filter'
numbers_list = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0))
print(f"Even numbers from the list: {even_numbers}")

print("\nEnd of Functions Demonstration!")

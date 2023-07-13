# Calculator App

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0: 
#         return "Error: Cannot divide by zero"
#     return a / b

# def calculator(): 
#     print("Welcome to the Calculator App!")
#     print("Operations: ")
#     print("1. Addition (+)")
#     print("2. Substraction (-)")
#     print("3. Multiplication (*)")
#     print("4. Division (/)")

#     operation = input("Enter the operation number: ")
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     if operation == '1': 
#         result = add(num1, num2)
#         operator = "+"
#     elif operation == '2': 
#         result = subtract(num1, num2)
#         operator = "-"
#     elif operation == '3': 
#         result = multiply(num1, num2)
#         operator = "*"
#     elif operation == '4': 
#         result = divide(num1, num2)
#         operator = "/"
#     else: 
#         print("Invalid operation selected")
#         return
    
#     if isinstance(result, str): 
#         print(result)
#     else: 
#         print(f"{num1} {operator} {num2} = {result}")

#     # Run the calculator app
#     calculator()


# Using the Flask framework to create a web app. 
# This code creates a calculator app using Python & Flask. 
# This web-based calculator allows users to perform basic arithmetic operations. 
# Run the Python script and access the app in a web browser at http://localhost:5000


from flask import Flask, render_template, request

app = Flask(__name__ )

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        operation = request.form["operation"]
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])

        if operation == "add":
            result = add(num1, num2)
            operator = "+"
        elif operation == "substract":
            result = substract(num1, num2)
            operator = "-"
        elif operation == "multiply":
            result = multiply(num1, num2)
            operator = "*"
        elif operation == "divide":
            result = divide(num1, num2)
            operator = "/"
        else:
            return "Invalid operation selected"

        if isinstance(result, str):
            return result
        else:
            return f"{num1} {operator} {num2} = {result}"
    else:
        return render_template("calculator.html")

if __name__ == "__main__":
    app.run(debug=True)






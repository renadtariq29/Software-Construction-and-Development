print("Simple Calculator")

num1 = float(input("Enter your first number: "))
operator = input("Enter the operation you want to perform (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operation")
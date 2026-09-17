def calculate(first_number, second_number, operation):
	if operation == "+":
		return first_number + second_number
	if operation == "-":
		return first_number - second_number
	if operation == "*":
		return first_number * second_number
	if operation == "/":
		if second_number == 0:
			return None
		return first_number / second_number
	return "invalid"


print("Calculator")
first_number = float(input("First number: "))
operation = input("Choose an operation (+, -, *, /): ")
second_number = float(input("Second number: "))

answer = calculate(first_number, second_number, operation)

if answer == "invalid":
	print("Invalid operation.")
elif answer is None:
	print("Cannot divide by zero.")
else:
	print("Answer:", answer)

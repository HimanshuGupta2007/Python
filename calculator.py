num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter +, -, * or /: ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
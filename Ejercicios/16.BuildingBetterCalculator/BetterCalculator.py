
num1 = float(input("Enter first number: "))
OP = input("Enter Operator: ")
num2 = float(input("Enter second number: "))

if OP == "+":
    print(num1 + num2)
elif OP == "-":
    print(num1 - num2)
elif OP == "/":
    print(num1 / num2)
elif OP == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
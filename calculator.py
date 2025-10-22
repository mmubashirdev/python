def calculator(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Divisor cannot be zero"
        else:
            return a / b
    else:
        return "Invalid operator"

num1 = int(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))

result = calculator(num1, op, num2)
print("Result:", result)

    
































# def add(a, b):

#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero!"
#     return a / b

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# if choice == '1':
#     print(f"Result: {add(num1, num2)}")
# elif choice == '2':
#     print(f"Result: {subtract(num1, num2)}")
# elif choice == '3':
#     print(f"Result: {multiply(num1, num2)}")
# elif choice == '4':
#     print(f"Result: {divide(num1, num2)}")
# else:
#     print("Invalid input")

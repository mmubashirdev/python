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

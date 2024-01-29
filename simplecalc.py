def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    print("Simple Calculator\n")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
    
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter choice (1/2/3/4): "))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice. Please enter a valid choice.")
        return

    if choice == 1:
        result = add(num1, num2)
        operation = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "/"

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()

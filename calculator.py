def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("=== Mini Calculator ===")

while True:
    print("\nOptions: add, subtract, multiply, divide, exit")
    choice = input("Enter option: ").lower()
    
    if choice == "exit":
        print("Exiting Calculator.")
        break
    
    if choice in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == "add":
            print("Result:", add(num1, num2))
        elif choice == "subtract":
            print("Result:", subtract(num1, num2))
        elif choice == "multiply":
            print("Result:", multiply(num1, num2))
        elif choice == "divide":
            print("Result:", divide(num1, num2))
    else:
        print("Invalid choice! Try again.")

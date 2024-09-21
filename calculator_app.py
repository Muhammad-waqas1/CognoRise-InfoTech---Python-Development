import operator

def calculator():
    ops = {
        '1': ('Addition', operator.add),
        '2': ('Subtraction', operator.sub),
        '3': ('Multiplication', operator.mul),
        '4': ('Division', operator.truediv)
    }
    
    print("Select operation:")
    for key, value in ops.items():
        print(f"{key}. {value[0]}")

    try:
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in ops:
            raise ValueError("Invalid operation selected.")
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '4' and num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        
        operation, func = ops[choice]
        result = func(num1, num2)
        
        print(f"The result of {operation} is: {result:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()

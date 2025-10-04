# Extended error handling for division

try:
    # Take input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform division
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
except EOFError:
    print("\nUnexpected end of input. Exiting...")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

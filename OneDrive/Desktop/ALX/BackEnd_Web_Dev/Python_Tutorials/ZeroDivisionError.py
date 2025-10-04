# Exercise 1: Handling ZeroDivisionError
try:
    # Take input from user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    # Perform the Division
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator")
except ValueError:
    print('Error: Invalid input. Please enter numeric values only. Thank You!')


# How it works: 1. The program asks the user for two numbers.
# 2. It tries to divide the first number by the second.
# 3.If the second number is zero, the ZeroDivisionError is caught and a friendly error message is shown instead of crashing.
# 4. If the user enters letters or symbols → program shows “Invalid input”.
# Otherwise, it prints the result correctly.

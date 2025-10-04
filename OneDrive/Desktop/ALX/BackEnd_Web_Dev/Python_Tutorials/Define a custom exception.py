# Define a custom exception
class ValueTooHighError(Exception):
    """Raised when the input value is greater than 100"""
    pass


def check_value(num):
    if num > 100:
        raise ValueTooHighError(
            f"Error: The value {num} is too high! Must be 100 or less.")
    else:
        print(f"The value {num} is accepted.")


# Main program
try:
    number = int(input("Enter a number: "))
    check_value(number)
except ValueTooHighError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter a numeric value.")

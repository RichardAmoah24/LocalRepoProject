day = input("Enter a day (Monday-Sunday)")
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's weekday...")
    case "saturday" | "sunday":
        print("It's weekend!")
    case _:
        print("This is not a day")

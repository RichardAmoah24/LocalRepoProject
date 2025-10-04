my_age = 31
guess_count = 0
guess = 0
while guess != my_age:
    guess_count += 1
    guess = int(input("Guess my age between 1 and 40: "))
print(f"You guessed it in {guess_count} tries!")

shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = False
while not item_found:
    item = input("Search for an item in your list (or 'q' to quit): ")
    if item.lower() == "q":
        break  # Exit the loop if user enters 'q'
    if item in shopping_list:
        item_found = True
        print(f"{item} is on your shopping list.")
    else:
        print(f"{item} is not on your list.")

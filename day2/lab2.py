import random
# 1
def sortNumbers(*args):
    """function to sort numbers enterd
    by user in asec and desc
    """
    num_list = []
    for i in args:
        if not isinstance(i, (int, float)):
            print(f"Invalid input: {i} is not a number.")
            return
        num_list.append(i)
    if not num_list:
        print("No numbers provided.")
        return
    num_list.sort()
    print(num_list)
    print("=" * 15)
    num_list.sort(reverse=True)
    print(num_list)


# 2
def twoNumbers(length, start):
    """Generate a sequence of numbers
        with the given length,
        starting from the given start number
        and increasing by one each time.
    """
    if not isinstance(length, int) or not isinstance(start, int):
        print("Both length and start must be integers.")
        return
    if length <= 0:
        print("Length must be a positive integer.")
        return
    num_sequence = []
    for i in range(length):
        num_sequence.append(start)
        start += 1
    print(num_sequence)


# 3
def numOperations():
    """The total of all numbers entered
    The count of valid entries
    The average
    """
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or 'done' when finish ): ")

        if user_input.lower() == "done":
            break

        try:
            num = float(user_input)
            total += num
            count += 1
        except ValueError:
            print(" Invalid input, please enter a number.")

    if count > 0:
        average = total / count
    else:
        average = 0

    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")


# 4
def distincitNums():
    """Ask the user to enter a list of numbers.
    Remove any duplicates, sort the result,
    and display it.
    """
    user_input = input("Enter numbers : ")
    try:
        arr = list(map(int, user_input.split()))
        arr = sorted(set(arr))
        print(arr)
    except ValueError:
        print("Invalid input, please enter only numbers .")


# 6
def wordCount():
    sentence = input("Enter sentence : ")
    if not isinstance(sentence, str) or not sentence.strip():
        print("Invalid input, please enter a non-empty sentence.")
        return
    words = sentence.lower().split()
    words_dict = {}
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
    for word, count in words_dict.items():
        print(f"{word}: {count}")


# 7
def gradebook():
    """ The user enters 5 students 
        names and their scores.
        At the end, show:
            * The highest score
            * The lowest score
            * The average score.
    """
    students = {}
    for i in range(5):
        while True:
            name = input(f"Enter name of {i+1}th :").strip()
            if not name:
                print("Name cannot be empty.")
            elif name in students:
                print("Duplicate name, please enter a unique name.")
            else:
                break
        while True:
            try:
                grade = float(input("Enter grade :"))
                if grade < 0 or grade > 100:
                    print("Grade must be between 0 and 100.")
                    continue
                break
            except ValueError:
                print("Invalid input , please enter a number")
        students[name] = grade
    grades = students.values()
    lowest = min(grades)
    highest = max(grades)
    average = sum(grades) / len(grades)
    print(f"Lowest grade : {lowest}")
    print(f"Highest grade : {highest}")
    print(f"Average grade : {average}")


# 8
def shoppingCart():
    """ simulates a shopping cart:
        - The user can add items with a name and a price.
        - The user can remove items by name.
        - The user can view all items with their prices.
        - At the end, display the total cost.
    """
    cart = []

    while True:
        print("--- Shopping Cart Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. totoal cost")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            name = input("Enter item name: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            while True:
                try:
                    price = float(input(f"Enter price for {name}: "))
                    if price < 0:
                        print("Price cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
            cart.append({"name": name, "price": price})
        elif choice == "2":
            name = input("Enter the item name to remove: ").strip()
            if not name:
                print("Item name cannot be empty.")
                continue
            removed = False
            for item in cart:
                if item["name"].lower() == name.lower():
                    cart.remove(item)
                    removed = True
                    print(f" {name} removed from cart.")
                    break
            if not removed:
                print(f"{name} not found in cart.")
        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                print("--- Items in Cart ---")
                for i, item in enumerate(cart, start=1):
                    print(f"{i}. {item['name']} - ${item['price']:.2f}")
        elif choice == "4":
            total = 0
            for item in cart:
                total += item["price"]
            if not cart:
                print("Your cart is empty.")
            else:
                for item in cart:
                    print(f"{item['name']} - ${item['price']:.2f}")
            print(f"Total cost: ${total:.2f}")
            break
        else:
            print("Invalid option, please choose 1-4.")


# 9

def guessingGame():
    """number guessing game:
        - The program randomly selects a number between 1 and 20.
        - The user has to guess the number.
        - After each guess, the program tells the user if the guess is too low, too high, or correct.
        - The game continues until the user guesses the correct number.
    """
    rand_num = random.randint(1, 20)
    attempts = 0

    while True:
        user_input = input("Enter your guess: ")
        try:
            guess = int(user_input)
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue
            attempts += 1

            if guess < rand_num:
                print(" Oops Too low ! Try again.")
            elif guess > rand_num:
                print(" Oops Too high!  Try again.")
            else:
                print(f" Correct! The number was {rand_num}.")
                break
        except ValueError:
            print(" Please enter a valid number.")
# guessingGame()

def main():
    options = {
        "1": ("Sort numbers", sortNumbers),
        "2": ("Generate sequence", twoNumbers),
        "3": ("Numbers operations (total-count-average)", numOperations),
        "4": ("Unique sorted numbers", distincitNums),
        "6": ("Word frequency counter", wordCount),
        "7": ("Gradebook", gradebook),
        "8": ("Shopping cart", shoppingCart),
        "9": ("Guessing game", guessingGame),
    }

    while True:
        print("--- Main Menu ---")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice. Please enter one of:", ", ".join(options.keys()), "or 0 to exit.")


if __name__ == "__main__":
    main()
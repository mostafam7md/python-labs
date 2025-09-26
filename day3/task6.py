import random

def random_data_generator():
    try:
        # Step 1: Ask user for how many numbers
        count = int(input("How many random numbers to generate? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if count <= 0:
        print(" Count must be greater than 0.")
        return

    # Step 2: Generate random numbers
    numbers = [random.randint(1, 100) for _ in range(count)] 

    # Step 3: Save to CSV file
    with open("./day3/random_numbers.csv", "w") as f:
        f.write("index,value\n")
        for i, num in enumerate(numbers, start=1):
            f.write(f"{i},{num}\n")

    # Step 4: Print summary
    average = sum(numbers) / count
    print(f"Generated {count} random numbers.")
    print(f" Average value: {average:.2f}")


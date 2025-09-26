from datetime import datetime

def datetime_reminder():
    """ Datetime Reminder
    """
    # Step 1: Ask user for a date input
    date_str = input("Enter a date (YYYY-MM-DD): ")

    try:
        # Step 2: Parse the input into a datetime object
        reminder_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()

        # Step 3: Calculate days difference
        delta = (reminder_date - today).days

        if delta < 0:
            # Past date
            print(" This date has already passed.")
        else:
            # Step 4: Save reminder into file (append mode)
            with open("./day3/reminders.txt", "a") as file:
                file.write(f"{reminder_date} -> {delta} days left\n")
            

    except ValueError:
        print(" Invalid date format! Please use YYYY-MM-DD.")


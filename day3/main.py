from task1 import mathAutomation
from task2 import regex_log_cleaner
from task3 import datetime_reminder
from task4 import product_data_transformer
from task5 import os_file_manager
from task6 import random_data_generator
from task7 import math_automation as decorated_fun1, regex_log_cleaner_decorated as decorated_fun2


def main():
    options = {
        "1": ("Math Automation", mathAutomation),
        "2": ("Regex Log Cleaner", regex_log_cleaner),
        "3": ("Datetime Reminder", datetime_reminder),
        "4": ("Product Data Transformer", product_data_transformer),
        "5": ("OS File Manager", os_file_manager),
        "6": ("Random Data Generator", random_data_generator),
        "7": ("Decorated Math Automation (with log_time)", decorated_fun1),
        "8": ("Decorated Regex Log Cleaner (with log_time)", decorated_fun2),
    }

    while True:
        print("\n--- Main Menu ---")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice in options:
            print(f"\n Running: {options[choice][0]} \n")
            options[choice][1]()
        else:
            print(" Invalid choice. Please enter one of:", ", ".join(options.keys()), "or 0 to exit.")


if __name__ == "__main__":
    main()

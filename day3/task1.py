import math
def mathAutomation() : 
    """ calculate:
        - floor
        - ceil
        - square root
        - area of a circle
    """
    # Step 1: Ask user for numbers separated by commas
    nums = input("Enter numbers separated by commas: ")
    # Step 2: Try converting input into a list of floats
    try : 
        nums = [float(num.strip()) for num in nums.split(",")]
    except ValueError :
        print("must enter numbers sperated by comma")
        return
    
    try:
        # Step 3: Open (or create) file for writing results
        with open(r"./day3/math_report.txt", "w") as file:
            for num in nums:
                ceil_num = math.ceil(num)
                floor_num =math.floor(num)       
                # Step 4: Handle square root safely (avoid crash on negatives)
                try:
                    sqrt_num = math.sqrt(num)
                except ValueError :
                    sqrt_num = "negative number"
                # Step 5: Calculate area of a circle using num as radius
                circle_area = math.pi * num * num
                # Step 6: Write all results into the file
                file.write(f"floor of {num} is : {floor_num}\n")
                file.write(f"ceil of {num} is : {ceil_num}\n")
                file.write(f"square root of {num} is : {sqrt_num}\n")
                file.write(f"area of the circle {circle_area}\n")       
        # Step 7: Try opening the file again to read and display results
        with open("math_report.txt", "r") as file:
            data = file.read()
            print(data)
        print("file not found!")
    except FileNotFoundError:
        print("Error while writing file")


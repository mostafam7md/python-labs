import time
from task1 import mathAutomation
from task2 import regex_log_cleaner

def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  
        end = time.time()
        runtime = round(end - start, 4)

        with open("./day3/execution_log.txt", "a") as log:
            log.write(f"{func.__name__} ran in {runtime} seconds\n")

        return result
    return wrapper


@log_time
def math_automation():
    """
    Runs mathAutomation() from task1 with execution time logging.
    """
    return mathAutomation()  


@log_time
def regex_log_cleaner_decorated():
    """
    Runs regex_log_cleaner() from task2 with execution time logging.
    """
    return regex_log_cleaner()  

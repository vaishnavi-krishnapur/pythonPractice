#Create a custom exception class called salarynotinrange, this should throw an exception when ever input salary is not in range of 100000-2000000 respectively
class CustomException(Exception):
    """Custom Exception raised"""

salary = 1000000
try:
    if not 100000 < salary < 2000000:
        raise CustomException()
    else:
        print("salary is good")
except CustomException as error:
    print("Salary Not in range. Exception raised")




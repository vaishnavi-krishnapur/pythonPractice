#Create a custom exception class. Write function F above except it should throw a warning when K>100.
class CustomException(Exception):
    """Custom Exception class"""

class Problem6(CustomException):
    def __init__(self,k):
        self.k=k
    def check(self):
        try:
            if self.k > 100:
                raise CustomException()
            else: print("All good")
        except CustomException:
            print("Custom Exception raise. K value is > 100")

obj= Problem6(1011)
obj.check()
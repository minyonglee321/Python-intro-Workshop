"""This is a very silly module."""
from datetime import datetime


def adding_two_numbers(a: float, b: float):
    """Adds two numbers"""
    return a + b

def get_todays_date():
    """Returns todays date"""
    today = datetime.now()
    return today

class Employee():
    """Creates an HA employee."""
    
    def __init__(self, fullname: str, age: int, knows_Python: bool):
        self.fullname = fullname
        self.age = age
        self.knows_Python = knows_Python

    def __str__(self):
        if self.knows_Python:
            return f'{self.fullname} knows Python and thus, is' + \
                ' an amazing employee.'
        else:
            return f'{self.fullname} is about to learn python and will be' + \
                ' an amazing employee.'
"""
A simple script that asks user for name and date of birth and prints how
many days user has been alive.
"""

from datetime import datetime


while True:
    try:        
        name = input('What is your name?\n')
        birth = datetime.strptime(input('When where you born?\n'), "%m/%d/%Y")
        today = datetime.now()
        days_alive = (today - birth).days
        print(f"{name} you've lived {days_alive} days!!")
        break
    except:
        pass
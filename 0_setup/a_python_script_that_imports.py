"A simple script that imports a module and call the functions in that module"

# Importing module
import a_python_module

# Running functions and create an instance of HAEmployee
print(a_python_module.adding_two_numbers(4, 5))
print(f"Today's date and time is: {a_python_module.get_todays_date()}")
lorenzo = a_python_module.HAEmployee('Lorenzo Peve', 26, knows_Python = False)
print(lorenzo)
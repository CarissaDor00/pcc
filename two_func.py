"""
Two functions, the first function asks the user for her name.
The second function uses the output of function one to greet the
user.
"""

def func1():
    """ This function asks for name."""
    name = input("What is your name? ")
    return name
result = func1()

def func2(user):
    """ This function greets the user."""
    
    print(f"Hey, {user} nice to meet you!")

func2(result)

func2(func1())

print(func2.__doc__)

"""
Two functions, the first function asks the user for her name.
The second function uses the output of function one to greet the
user.
"""

def get_name():
    """ This function asks for name."""
    name = input("What is your name? ")
    return name
result = get_name()

def greet_user(user):
    """ This function greets the user."""
    
    print(f"Hey, {user} nice to meet you!")

greet_user(result)

greet_user(get_name())

print(greet_user.__doc__)

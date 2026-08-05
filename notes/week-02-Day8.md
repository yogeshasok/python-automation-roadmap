function 

it should be defined with keyword def and it holds set of instruction that need to be run

def my_method()

arguments:
*args -->  Use *args when you do not know in advance how many positional inputs a user will pass to your function

def add_all_numbers(*args):
    # args behaves exactly like a normal tuple
    return sum(args)

# You can pass any number of inputs
print(add_all_numbers(10, 20))        # Output: 30
print(add_all_numbers(1, 2, 3, 4, 5))  # Output: 15



**kwargs --> Use **kwargs when your function needs to handle named arguments that haven't been predefined in the signature

def print_user_profile(**kwargs):
    # kwargs behaves exactly like a normal dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_profile(username="dev_jane", role="Admin", active=True)
# Output:
# username: dev_jane
# role: Admin
# active: True


*args should come first and **kwargs should come second 

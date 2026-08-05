Variable Scope
The LEGB rule defines the exact order in which Python searches for variable names during execution
L - Local
E - Enclose
G - Global
B - Builtins

Local:
Variables defined inside the current function or lambda expression. Only visible inside that function

def my_func():
    x = "Local"  # Local Scope
    print(x)


Enclose:
Variables inside an outer function that wraps around a nested inner function. Accessible by the nested inner functions.

def outer_func():
    x = "Enclosing"  # Enclosing Scope
    def inner_func():
        print(x)  # Looks up to outer_func


Global:
Variables defined at the top level of a script, module, or file. accessible from anywhere within module

x = "Global"  # Global Scope

def my_func():
    print(x)


Builtins:
Pre-defined keywords, functions, and exceptions built directly into Python. Always available without any import statments
print(), len(), range(), and dict

First-Class Functions
Nested Function --> function inside function

def outer():
  print("Outer function")
  def inner():
    print("Inner function")

outer() //only outer function will be printed

def outer():
  print("Outer function")
  def inner():
    print("Inner function")
  inner()

outer() // print both inner and outer function



Returing Function --> we will return function itself

def outer():
  print("Outer function")
  def inner():
    print("Inner function")
  return inner

outer() // print outer function and nothing, but if we store it in some variable
func_obj = outer()
func_obj() // print inner print statements


Closure -->
 Closure is a function that remembers the variables from its enclosing scope, even after outer function has finished executing

 def outer(num):
  print("Outer function")
  def inner():
    print("Inner function")
    print(num)
func_obj = outer() //print outer function
func_obj() // print inner print statement and num (variable num is accessible even when we are calling inner function directly 

func_obj = outer() //print outer function
del outer
func_obj() // still prints num because everything already scoped

Function passed as arguments -->

def add(a, b):
  return(a+b)

def sub(a, b):
  return(a-b)

def calculate(func_met, a, b):
  return func_met(a,b)

print(calculate(sum, 20, 10))

Function can be store in data structure -->

def add(a, b):
  return(a+b)

def sub(a, b):
  return(a-b)

function_dict = {
  "add" : add(20,10),
  "sub": sub(20,10)
}

function_dict['add'] // will call add function

function_dict = {
  "add" : add,
  "sub": sub
}
function_dict['add'](20,10)


## Lambda functions
small ananyms function , can take any number of arguments but have only one expression, using keyword lambda

lambda <argum>: <expression>

cal = lambda (a, b): a+ b

cal(10,20)


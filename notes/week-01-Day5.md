## Comprehension

A comprehension in Python is a short way to build a new data structure (like a list, set, or dictionary) from an existing collection using a single line of code. It replaces multiple lines of for loop and append() logic with a clean, readable statement

List Comprehension: Makes a new list using square brackets []. Example: [x * 2 for x in range(5)]

Dictionary Comprehension: Makes a dictionary using curly braces {} with key-value pairs. Example: {x: x * 2 for x in range(5)}

Set Comprehension: Makes a set using curly braces {}, which drops duplicates. Example: {x for x in [1, 2, 2, 3]}

Generator Expression: **Uses parentheses ()** to save memory by yielding items one by one. Example: (x * 2 for x in range(5))

Genrator is also iterable object like list, set. we can get values by calling next() to yield it return one value when we call everytime. So whole data will not be stored in memory. 

def yielding_values():
  yield "hello"
  print("This is print statement")
  yield "welcome to my learning session"

first = yielding_values()

print(next(first)) // it yields "hello" and store the end point, print statment will not executed

print(next(first)) // prints both print statement and print yield message, if no more values are there, it throws stopIteration error. To fix this, we need to enclose in try except block (except StopIteration)

gen_values = (num for num in range(1,10))

print(next(gen_values)) //1
print(next(gen_values)) //2

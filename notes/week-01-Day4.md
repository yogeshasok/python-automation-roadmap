----------------------------
Structural Pattern
------------------------------

unpack an interable 

head, *middle, tail = range(10)

Unpacking and merge dictionaries

{**headers, **cookies}

Access a value by index last_item = items[-1]

Acess a value by key path = os.environ['PATH']

Access an attribute by name date = datetime.date

pattern Matching :
match takes subject
case introduce a pattern to compare against

match subject:
	case list([int() | float() as x, int() | float as y, 0]):
		print(f"Point ({x=},{y=})")
		
		
When to use Structural Pattern Matching
	Data Structures are complex or nested
	Decision are made based on parts of the data, with destructing
	Patterns to match are largely exclusive of each other
	Conditions are not based on complete business rules requring lots of computation
	
Literal Pattern
Value Patterns (Constant Values)
WildCard -- matches to any subject

match subject:    // Python Literals bytes, str, int, float, complex, bool, NoneType . match by Equality (==), identity(is)
	case "Phython":
		print("It's Python")
	case 42:
		print("It's 42")
		
Value Patterns -- constants , can be achieved using classes, enum or namespace

class Subject:
	PHYTHON = "Python"
	FORTYTWO = 42
	
match subject:
	case subject.PYTHON:
		print("It's Python")
	case subject.FORTYTWO:
		print("Its 42")
		
WildCard Pattern:

uses _ as pattern

match subject:
	case _:
		print("It's anything")
		



--------------------------------
Walrus Operator
--------------------------------

Introduced in Python3.8

Assignment expression

if (n := len(a)) > 10:
	print(f"List is too long ({n} elements, expected <=10)")
	
	
def get_input_length():
	user_input = input("Enter something")
	length = len(user_input)
	if length > 0:
		print(f"Entered input length is {length} characters")
if __name__ == "__main__":
	get_input_length()
	
	
Using Walrus operator:
def get_input_length():
	user_input = input("Enter something")
	if ( length := len(user_input)) > 0:
		print(f"Entered input length is {length} characters")
	
def loop_numbers():
		numbers = [1,2,3,4,5]
		n = len(numbers)
		while n > 0:
			print(f"Popped numbers from list")
			numbers.pop()
			n = len(numbers)

Using walrus operator:
def loop_numbers():
	numbers = [1,2,3,4,5]
	while(n := len(numbers)) > 0:
		print(f"Popped numbers from list")
		numbers.pop()
		
List Comprehensions with walrus operator:
[clean_name.title() for name in names if (clean_name := normalize('NFC', name)) in allowed_names]



import json

def parse_json(string):
	try:
		return json.loads(string)
	except:
		return None
		
if '__name__' == '__main__':
	raw_data = ['{"name":"Jenn"}','invalid','{"age":30}', '{badjson}']
	parsed_items = [
		obj for string in raw_data if (obj := parse_json(string)) is not None
	]
	print(parsed_items)
	


```
message = 'Hello World'
message = "Hello World"
message = 'It\'s my place'
message =  """ Hello world
By user"""
print(message)
```

To slice the string **string[start:end(will not include end character)]**
```
message = 'Hello World'

print(message[0:5]) //prints Hello H->0, e->1, l->2, l->3, 0->4.
print(message[:5]) //start will be considered as 0, so same will be printed
print(message[6:]) //Starts with 6th and print remaining complete so **World**
```
Methods for String :
```
print(message.lower()) // all lowercase
print(message.upper()) //all uppercase

print(message.count('Hello')) // print occurance of word

print(mesage.find('world')) // Returns 6, as it start index. if not present return -1

print(message.replace('Hello', 'Hey') //Replace Hello with Hey ** not inplace replacement, so it will print Hello World only**

new_message  = message.replace('Hello','Hey') or message = message.replace('Hello', 'Hey')

greeting = 'Hello'
name = 'yogesh'

message = greeting + name // Helloyogesh

message = greeting + ', '+ name //Hello, yogesh

message = greeting + ', '+ name+ '. Welcome!' // Hello, yogesh. Welcome!

message = '{}, {}.Welcome!'.format(greeting, name) //String Formatting

python 3.6+ > will support fString

message = f'{greeting}, {name}. Welcome!'

print(dir(name)) //print all attributes and methods available

print(help(str)) //print description about the methods present in String

print(help(str.lower()) //print information about lower methods for string

```

### Advance String Formatting:
```
person = { 'name': 'Jenn', 'age': '32'}

sentence = 'My name is {} and i am {} years old'.format(person['name'], person['age'])
sentence = 'My name is {0} and i am {1} years old'.format(person['name'], person['age']) //numbered string formatter

sentence = '<{0}>{1}</{0}>'.format(person['name'], person['age'])


sentence = 'My name is {0[name]} and i am {1[age]} years old'.format(person,person)

sentence = 'My name is {0[name]} and i am {0[age]} years old'.format(person)

l = ['Jenn',23]

sentence = 'My name is {0[0]} and i am {0[1]} years old'.format(l)

Class Person():
	def __init__(self, name,age):
		self.name = name
		self.age = age

p1 = Person('Jenn',23)
sentence = 'My name is {0.name} and i am {0.age} years old'.format(p1)


sentence = 'My name is {name} and i am {age} years old'.format(name='Jenn', age='30')

sentence = 'My name is {name} and i am {age} years old'.format(**p1) // Unpacking Dictionary  ** 


Formatting numbers Integers

for i in range(1,11):
	sentence = 'The Value is {0}'.format(i)
	print(sentence)

for i in range(1,11):
	sentence = 'The Value is {:02}'.format(i) // 01 02 03, if :03, then 001 002 003
	print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {:.2f}.format(pi) --> to print only two digits after decimal


sentence = 'Pi is equal to {:,}.format(1000**2) --> 1,000,000

sentence = 'Pi is equal to {:,.2f}.format(1000**2) --> 1,000,000.00

import datetime
mydate = datetime.datetime(2016, 9 ,24,12,30,45)
print(mydate)

sentence = '{:%B %d, %Y}'.format(mydate) //September 24, 2016
```
________________________________________________________________________________________________________________
________________________________________________________________________________________________________________
## Integer and Float
```
num = 2

print(type(num)) //Integer

num = 3.4 
print(type(num)) //Float

print(3 / 2) --> 1 in python2 and 1.5 in python 3

print(3 % 2) --> remainder

print(3 // 2) --> floor divison

print(3 ** 2) --> 3^2


print(abs(-3)) --> 3 absolute value

print(round(3.75)) --> 4
print(round(3.75, 1)) --> 3.8 1st digit after dot

```


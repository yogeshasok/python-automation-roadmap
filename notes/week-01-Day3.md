----------------------------------------------------
Dictionary
----------------------------------------------------
**Key Value pair**
```
student = {'name':'Jenn', 'age':24, 'courses':['Math', 'ComputerSc']}

print(student['name'])

print(student['email']) --> key error 
print(student.get('email')) --> return None

print(student.get('email','NotFound')) -->return NotFound
```
### To update dict
```
student['email'] = 'abc@gmail.com'
student['name'] = 'John'

student.update({'name':Jenn, 'age':29, 'email':'xyz@gmail.com'})
```
### To delete specific key value
```
del student['age']

age = student.pop('age')
```

### To loop through values and key
```
print(len(student)) --> 3 keys

print(student.keys())

print(student.values())

print(student.items())
for key in student:
	print(key)
	
for key, value in student.items():
	print(key, value)
	
```	
	
-------------------------------------------------------------------
Collections - Counter, namedtuple, OrderedDict, defaultdict, deque
___________________________________________________________________

## Collections
** for collections import Counter --> stores result in key value pairs **
```
a = 'aaaabbbccccdd'

my_counter = Counter(a)

print(my_counter) // Counter({'a':4, 'b':3, 'c':4, 'd':2'})

print(my_counter.most_common(1)) --> 1st most common [('a',4),('c',4)]

```
## namedtuple
```
from collections import namedtuple //similar to Struct
Point = namedtuple('Point','x,y') //create classs with x and y

pt = Point(1,-4)

print(pt)

print(pt.x)
print(pt.y)
```

## OrderedDict // Remember the order how it got inserted
```
from collections import OrderedDict // python3.7 + normal dictionary itself will remember the order

order_dict = OrderedDict()

order_dict['name'] = 'Jenn'
order_dict['age'] = 23
order_dict['email'] = 'abc@gmail.com'
```

## defaultdict
```
from collections import defaultdict //similar to normal dictionary onlything is it will have default value if it doesn't have values
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a])

print(d['c']) //key not there, but it will return default value of type interger (0)
```

### deque
from collections import deque //double ended queue, can add remove in both end
```
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(d)

d.appendleft(5)
d.pop()
d.popleft()
d.clear() --> clear all elements
d.extend(<list>)
d.extend([5,6,7])
d.extendright([5,6,7])
```
d.rotate(-1) //rotate left side


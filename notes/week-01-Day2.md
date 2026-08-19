----------------------------------------------------
Lists, Tuples, Sets, Frozensets
----------------------------------------------------
```
courses = ['History', 'Math', 'Physics', 'ComputerSci']

print(courses[-1]) //Last one

print(courses[0:2]) // History Math

print(courses[:2]) //History Math

print(courses[2:]) //Physics ComputerSci
```
## List Methods:

### Add items to list 
```
courses.append('Art')

print(courses) //Appended at end
```
### insert at specific index
```
courses.insert(0,'Art') 1st position is index and 2nd is value
```

### Extend if we want to add multiple value to list
```
courses_2 = ['Art', 'Education']

courses.insert(0,courses_2) 0th index will have list even append also does same at the end

courses.extend(courses_2) --> correct way to add 
```

### Remove
```
courses.remove('Math')

course = courses.pop() --> remove last value in list
```

### Sorting 
```
courses.reverse() --> reverse order

courses.sort() --> alphabetic order sort

num = [1,5,4,2,3]

num.sort() --> ascending order
num.sort(reverse=True) --> opposite order

sorted_courses = sorted(courses) --> sort without affecting original
```
### Min, Max, Sum
```
print(min(num)) --> 1
print(max(num)) --> 5
print(sum(num)) --> 15
```
### Find Values in list
```
print(courses.index('ComputerSci')) it will return index if not found it return error
```

### to get boolean result 
```
print('Math' in courses)
```

```
for course in courses:
	print(course)
	
	
for index, course in enumerate(courses):
	print(index, course)
	
for index, course in enumerate(courses, start=1) //index starts with 1 instead of 0
	print(index, course)
course_str = ','.join(courses) //Commo seperated

new_list = course_str.split(',') // To split into list
```

## Tuples --> similar to list but not changeable. we cannot update the tuple and **it enclosed with ()**

```
courses = ('History', 'Math', 'Physics', 'ComputerSci')
```

**Everything same to list**

## Set --> Similar to set and tuples but enclosed with curly {}
```
courses = {'History', 'Math', 'Physics', 'ComputerSci'}
```
Order changes everytime and only one is allowed no duplicate values
```
courses_1 = {'History', 'Math', 'Physics', 'ComputerSci'}
courses_2 = {'History', 'Math', 'Art', 'Design'}
```
To get common courses between two sets, use intersect function
```
print(courses_1.intersection(courses_2)) //prints only History and Math
print(courses_1.difference(courses_2)) //only print difference Physics and ComputerSci

print(courses_1.union(courses_2)) //print all courses removing duplicates
```

Empty List [] or list()
Empty Tuples () or tuple()
Empty Dict {} --> Wrong, its dict
           set() --> correct way to create set
	

 
---------------------------------------------------------------
Sorting List Tuples Set 
---------------------------------------------------------------
```
li = [9,4,2,8,10,7,1,0]
s_li = sorted(li) --> returns new sorted list, so we have to assign to new list

s_li = sorted(li, reverse=True) --> Opposite order

tuple.sort() won't work since it does have

sorted() can be used in all data types. for dictionay , it sorts based on key

li = [-6, -4, -8, 0, 7, 5]

s_li = sorted(li) // -8 -6 -4 0 5 7

s_li = sorted(li, key=abs) //absolute value so output will be 0 -4 5 -6 7 -8

class employee:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary
	def __repr__(self):
		return('{},{},${}'.format(self.name, self.age, self.salary)
		
e1 = employee('Carl', 37, 70000)
e2 = employee('Sarah', 29, 67000)
e3 = employee('John', 43, 90000)

employees = [e1,e2,e3]

s_employees = sorted(employees) // gives error since sorted function doesn't what to use for sorting
```

To fix this, we have to write new function
```
def e_sort(emp):
	return emp.name

s_employees = sorted(employees, key=e_sort)

s_employees = sorted(employees, key=e_sort, reverse=True)

s_employees = sorted(employees, key=lambda e: e.name)

from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('age'))
```



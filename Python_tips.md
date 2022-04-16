# Imperative vs Declarative Programming difference
Imperative means 'HOW' (All the steps on how to acheive a result).
Declarative means 'WHAT' (People also means 'good' by declarative)
https://www.youtube.com/watch?v=E7Fbf7R3x6I&ab_channel=uidotdev


### Asyncio: Understanding Async / Await in Python
https://www.youtube.com/watch?v=bs9tlDFWWdQ

### Creating a Context Manager :
https://www.geeksforgeeks.org/context-manager-in-python/
#### When creating context managers using classes, user need to ensure that the class has the methods: __enter__() and __exit__(). The __enter__() returns the resource that needs to be managed and the __exit__() does not return anything but performs the cleanup operations.

##### Python program showing file management using context manager

```python
class FileManager():
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_value, exc_traceback):
		self.file.close()

# loading a file
with FileManager('test.txt', 'w') as f:
	f.write('Test')

print(f.closed)
```

##### Difference between Packages and modules
- Packages are also modules but they are generally directories and modules are files.
- type shows both as modules
- Packages have __path__ attribute while module doesn't

#### Timeit
```python
timeit.timeit('l.index(999_999)', setup='l = list(range(0, 1_000_000))', number=1000)
```
- **stmt:** which is the statement you want to measure; it defaults to ‘pass’.
- **setup:** which is the code that you run before running the stmt; it defaults to ‘pass’.We generally use this to import the required modules for our code.
- **timer:** which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
- **number:** which is the number of executions you’d like to run the stmt.

### BEST PRATICES
https://www.youtube.com/watch?v=ZdVgwhHXMpE  
#### PEP 20 | Explicit is better than implicit.
1. Don't use \__bool__  to add implicit trueness or falseness  
if len(user) > 0: # __this is good__  
if user > 0: # __this is good__  
if user: # __this is bad because there is no indication of why type of object it is :(__  

#### DON'T use exec or eval.
2. Because of eval or exec re-running to compile process i.e. (string -> Token (Lexical token)-> AST(Abstract syntax tree) -> bytecode -> run)  is a expensive process.

#### Repr over str
3. repr() produces an unambigous(by this we means type of the object along with any identifying fields) representation of an object. and a common guidline for a good repr is that it should display legitimate source code which when run can recreate the object. like Point2D(x={}, y={}) is create a new Point2D object with correct parameters.
Other way of thinking is repr is good for exactness, logging and debugging.
For e.g.
```python
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)
```		
#### Force format to use repr or str representation
Format defaults to str.
``` python 
    {!r}.format(Point(7,8)) # To use repr
    {!s}.format(Point(7,8)) # To use string
```

**String vs Repr Representation \_\_repr\_\_ vs \_\_str\_\_**:    
- str is generally a little more human friendly, repr is generally more precise.
- In str.format, !s chooses to use str to format the object whereas !r chooses repr to format the value.
```python
'foo {}'.format('bar')
'foo bar'
'foo {!r}'.format('bar')
"foo 'bar'"
```


**Recursion:**  
https://www.youtube.com/watch?v=AfBqVVKg4GE

**Scopes (LEGB):**   
**Local:** Inside the current function.    
**Enclosing:** Inside enclosing functions.   
**Global:** At top level of module.   
**Built-In:** In the special builtins module.   

What Does It Take To Be An Expert At Python? (https://www.youtube.com/watch?v=7lmCu8wz8ro&t=3551s)  
Core Python: Getting Started (https://app.pluralsight.com/library/courses/getting-started-python-core).   
Python – Beyond the Basics (https://app.pluralsight.com/library/courses/python-beyond-basics).  
Advanced Python (https://app.pluralsight.com/library/courses/advanced-python).  

**MetaClasses:**     
``` python
class Widget:
	pass
# Also means
class Widget(object, metaclass=type): #both object and metaclass are passed implicitly
	pass
```	
**Named Tuple:**  
Named tuples have the advantage that they provide a way to access their values using field names and the dot notation. This will make your code more Pythonic.
``` python
from collections import namedtuple

Person = namedtuple("Person", "name children")
john = Person("John Doe", ["Timmy", "Jimmy"])
john # Person(name='John Doe', children=['Timmy', 'Jimmy'])
john.children.append("Tina") # Person(name='John Doe', children=['Timmy', 'Jimmy', 'Tina'])
```
**Object orientation:**
- https://app.pluralsight.com/library/courses/core-python-classes-object-orientation
- Behaviour vs Data classes (https://www.youtube.com/watch?v=vRVVyl9uaZc):
	-  Some classes are mostly containers of behaviour e.g. class to draw a shape.
	-  Some classes acts more like containers of data e.g. class to represent a polygonal mesh e.g. a vehicle


**Principles of Object Oriented Design:**
- **SOLID** accronym:
	- Single Responsibility (**Class should have only one responsibility for e.g. cooking or washing up but not both**)
	- Open-Closed (**class should be open to be extension usually by inheritance but closed for modification**)
	- Liskov substitution (**Subclasses should be stand in for their parents without breaking anything**)
	- Interface segregration (**Many specific interface is better than one do it all interface**)
	- Dependency Inversion (**We should programs towards abstraction not implementation**)

**Design Patterns:**
https://app.pluralsight.com/library/courses/python-design-patterns/


**Error Handling:**    
- Avoid adding type checks for e.g. isinstance alternatively you can use except .
- Errors are like bells if we make them silent they are of no use.
- 'Finally' runs not matter if an exception was raise or not, so it can be used as try/execpt/finally or try/finally(If we don't want to handle the error)
- Look before you leap (LBYL) vs Easier to ask for forgiveness Than permission (EAFP)
	- Python **recommands using EAFP** 
		```python
		#LBYL Approach
		import os
		p = 'path/to/datfile.dat'
		#there can be many error which are possible so we will have to handle everything
		if os.path.exits(p):
			process_file(p)
		else:
			print(f"No such file as {p}")
		#EAFP Approach
		try:
			process_file(p)
		except OSError as e:
			print(f"Error {e}")
		```
# Polymorphism:		
    - Python program to demonstrate in-built polymorphic functions
  
    - len() being used for a string
    print(len("geeks"))
  
    - len() being used for a list
    print(len([10, 20, 30]))

# @property is used to set a method to behave as a attribute
E.g.
```python

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
```

# Super() in python:

https://www.programiz.com/python-programming/methods/built-in/super

Super behaves normaly for single inheritance i.e. to access methods of the base class. Whereas for multiple inheritance, like diamond inheritance below it follows the method resolution order(MRO), which can checked with ClassName.`__mro__` . E.g. `Dog.__mro__`

``` python
class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')

Output
Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.

Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.

Dog.__mro__
(__main__.Dog,
 __main__.NonMarineMammal,
 __main__.NonWingedMammal,
 __main__.Mammal,
 __main__.Animal,
 object)
```
# Note on class variables
It is best practice to use a class name to change the value of a class variable. Because if we try to change the class variable’s value by using an object, a new instance variable is created for that particular object, which shadows the class variables.

```python
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

# create Objects
s1 = Student('Emma', 10)
s2 = Student('Jessa', 20)

print('Before')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# Modify class variable using object reference
s1.school_name = 'PQR School'
print('After')
print(s1.name, s1.roll_no, s1.school_name)
print(s2.name, s2.roll_no, s2.school_name)

# Before
# Emma 10 ABC School 
# Jessa 20 ABC School 

# After
# Emma 10 PQR School
# Jessa 20 ABC School

```
 # Pass by reference vs by value
 ``` python
 myvar = 100
 my2var = myvar
 id(myvar)
 id(my2var)
 def primitive_are_pass_by_reference(x):
    """ x does not changes outside this function """
    x = x-1
 def non_primitive_are_pass_by_value(x):
    """ x changes outside this function """
    x.pop()
 ```

# Python -m flag
```python
# Python -m moduleTorunDemo 1stArg 2ndArg
# Export this folder in syspath
# export PYTHONPATH="/Users/adips/Desktop/Notes-ToDos/rough_work"
# 
import sys
print("Doing something")
print(sys.argv)
```
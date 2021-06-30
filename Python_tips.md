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

#### Force format to use repr or str representation
Format defaults to str.
``` python 
    {!r}.format(Point(7,8)) # To use repr
    {!s}.format(Point(7,8)) # To use string
```
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
3. repr() produces an unambigous(by this we means type of the object along with any identifying fields) representation of an object.

#### Asymptotic Analysis (Big-O(worst case), Big-Omega(best case) Notation). 
**Big-O notation:** is the performance of an algorithm when an input approaches upper limit.  
**O(n+1) is same as O(n)** because the curve will still remain the same as variable 'n' is same.  
**O(2n) is same as O(n)** because both have the same linear growth, so we can say constant multiplier are also ignored.  
**Ο(1)** The cost of this algo is same regardless of the input size (Don't confuse fixed cost with fast).  
**Ο(log n)** The cost of these algo does not increase, as the same rate as the input grows. These work by dividing a large problem in small and smaller chunks.  
**O(n<sup>2</sup>)** are the algo where the resource usage is the squared of input. E.g. is the doubly nested loop on the same array.  
**Examples:** 
Suppose if we have to search through a collection of one million record and we have 0(1) of 1m, Than 🤪
| Big-O notation | Elapsed time | 
| -------------   | ---------- |
|0(1) |  1ms |
|O(log n) | 6 ms | 
|O(n) | 16 min | 
|O(n<sup>2</sup>)| 11 days | 
|O(n<sup>3</sup>) | 31 million years |

Quick sort has worst case complexity of O(n<sup>2</sup>) but an average complexity of o(nlogn). This makes it good general purpose sorting algo but we should also be aware about the worst case scenario aswell.   

Following is a list of some common asymptotic notations − 
|Name | Big-O Notation |
| ------------  | ---------- |
| constant	|	Ο(1) | 
| logarithmic	|	Ο(log n) |
| linear	|	Ο(n) |
| n log n	|	Ο(n log n) |
| quadratic	|	Ο(n<sup>2</sup>) |
| cubic	|	Ο(n<sup>3</sup>) | 
| polynomial	|	n<sup>Ο(1)</sup> |
| exponential	|	2<sup>Ο(n)</sup> |

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
**Principles of Object Oriented Design:**
- **SOLID** accronym:
	- Single Responsibility (**Class should have only one responsibility for e.g. cooking or washing up but not both**)
	- Open-Closed (**class should be open to be extension usually by inheritance but closed for modification**)
	- Liskov substitution (**Subclasses should be stand in for their parents without breaking anything**)
	- Interface segregration (**Many specific interface is better than one do it all interface**)
	- Dependency Inversion (**We should programs towards abstraction not implementation**)

**Design Patterns:**
https://app.pluralsight.com/library/courses/python-design-patterns/

**String vs Repr Representation \_\_repr\_\_ vs \_\_str\_\_**:    
- str is generally a little more human friendly, repr is generally more precise.
- In str.format, !s chooses to use str to format the object whereas !r chooses repr to format the value.
```python
'foo {}'.format('bar')
'foo bar'
'foo {!r}'.format('bar')
"foo 'bar'"
```
**Error Handling:**    
- Avoid adding type checks for e.g. isinstance alternatively you can use except 
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

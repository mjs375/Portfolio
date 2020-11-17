# TESTING & DEBUGGING

## Manual Tests
-

### ```Print()```
- *the simplest debugger, simply place several ```print()``` statements in your code to examine the computations at each step of your program to ensure it is behaving as you want.*
  - ```print(f"Variable 'x' at step 3 is {x}."```
  
### Python Interpreter
- ``` $ python3```: *pull up the Python interpreter, where you can run or write Python code.*
- ``` $ from prime import is_prime```: *import your own functions [is_prime() from prime.py] to test.*
  - ```quit()```: *exit the interpreter*
```bash
mjs $ python3
Python 3.8.2 (...)
>>> from square import square
>>> square(10)
100
>>>
```  





### ```Assert```
- *the assert command tests whether a given function (and supplied parameters) evaluates to ```True```. If it does, nothing will happen, but if it is ```False```, an exception will be thrown.*

<table><tr><th>Python</th><th>Console</th></tr><tr><td>

```python
def square(x):
  return x + x   # <- BUG 
  # return x * x # <- fixed code
assert square(10) == 100
```

</td><td>

```terminal
Traceback (most recent call last):
  File "assert.py", line 3, in <module>
    assert square(10) == 100
  AssertionError
```

</td></tr></table>


### Test-Driven Development
- *every time you fix a bug (or add a new feature)*

























<hr>
<hr>


  
- ```try:``` ... ```except:```: *'Try' some code, while the 'Except' code will be run if any Error is encountered (specify a specific error: ```Except IndexError:```)* 
  - ```try: except: finally```: *Try will attempt some code, Except will activate if Try fails... and Finally will run its code along with Try or Except anyway.*
  - ```try: except: else:```: *if no Error is encountered in the Try block, it and the Else branch will run.*
 
  

- **Test-Driven Development**: *everytime you fix a bug, you add a test that checks for that bug to a growing list of bug-tests. Thus, anytime you add an additional feature, you run the tests and check for any bug-relapses. Run the test.py file from the Python interpreter to easily provide some input parameters (thing to test) and some expected values (what it should equal/return).*
  - ```$ python``` *open the Python interpreter*
  - ``` >>> from tests import test_function``` *import the test_function*
  - ``` >>> test_function(5, True)``` *run the test_function (which itself runs the original function), giving it an input and expected return value.*
  - *if n!= expected:* ```ERROR on...``` *if the return != expected, then a message will be printed*
``` 
<<tests.py>> #test file_name
from <file> import <func> #import the func to run tests on (original program)
  def test_function(n, expected):
  if func(n) != expected: # checks: does func(n) return what we expect?
    print(f"ERROR on func({n}), expected {expected}") # print statement when expected is not met
```
  
- **Shell Script**: *Automate many testings at once in a shell script, extension: ```.sh```. Overall, you'll have the original file ```function.py``` with the program, the ```test.py``` file, and a shell script ```tests.sh```. Shell scripts simply contain many terminal commands to execute, all-in-one. ```python3``` is which version of Python, ```-c``` means we intend to run a command, and the ```"..."``` includes the command in a string format*
  - Run these script commands by running ```./tests.sh``` in the terminal: will execute all shell commands at once, and print out the same "ERROR on..." statement if particular test fails.
```
python3 -c "from tests import test_prime; test_prime(1, False)"
python3 -c "from tests import test_prime; test_prime(2, True)"
    # and so on, as many tests as you want.
```

- **Unittest**: *Python's unnittest library.*
```
<<testings.py>> # filename 
import unittest 
from filename import function_name # function you are debugging
class Tests(unittest.TestCase): # a class containing all tests
  def test_1(self): # testing '1' (must be named 'test_'-something)
  """Check that 1 is not prime.""" # 'docstring' will display when test fails to help debug
  self.assertFalse(is_prime(1)) # self.assertSOMETHING (assertTrue, assertEqual, assertGreater...)
  
  def test_2(self): # testing '2'
  """Check..."""
  self.assertTrue(is_prime(2))
  
if __name__ == "__main__": # Run each of the testing functions:
  unittest.main()
```
  - ```$ python3 testings.py```
    - *Unittest will then spit out to the terminal console some information on the test results. It will start with something like ```...F.F```, which means 'Pass-Pass-Pass-Fail-Pass-Fail'. Then, for each failed test, it will give the name of the test and the docstring description, and a Traceback.*
  
- ```pdb```: *Python's built-in debugger tool, activated from the cmd-line. It runs line by line, showing the code in the console, per your keystroke. At any point ask pdb to show the values of variables instead of the code.*
  - *To run:* ```$ python3 -m pdb filename.py```
    - *Next line of code: press* ```n```
    - *Check full code: press* ```l```
    - *Check variable value: press* ```p``` *and* ```variable_name```






- **Django Server-side Testing**: *use the provided 'tests.py' to run test cases and check for bugs. Add a ```def is_valid_(self):``` test to the class, and/or more in ```test.py```. This will test whether certains functions work as we want.*
  - ```$ python3 manage.py test```: *output is akin to Python's unittest, it will log something like '..FF.F' to show Pass/Fail. Importantly, when this command is run it will 1. create a test database (using your dummy data), 2. run the tests, and 3. destroy the test database.*
```
class class_nameTestCase(TestCase):
  a = Airport.objects.create(code="AA", city="A") # Create dummy data:
  Flights.objects.create(origin=a, destination=b, duration=100) # create dummy data
  # Define some tests to run on the dummy data:
  def test_whattotest(self):
  a = Airport.objects.get(code="AA")
  self.assertEqual(a.departures.count(),3)
```
- More complicated testing [CS50 Notes](https://cs50.harvard.edu/web/2020/notes/7/):
  - **Django Client Testing**: *test whether individual web pages load as intended, simulating the making of requests.*
  - **Selenium**: *test out the client-side code, i.e. the HTML/Javascript on a webpage. Selenium framework simulates opening a web browser in the terminal, using a Web [Chrome]Driver.*

  

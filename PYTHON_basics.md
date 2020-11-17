# P Y T H O N  •  B A S I C S 
## TUTORIAL
- Indentation matters in Python: *it indicates a discrete block of code, such as what is contained in an ```if x>1:``` statement, what is inside a ```function(a)```, a for loop, &c. Once out of the block, de-dent back.*
- Zero-Indexing: *in Python, when counting elements of an entity, you must count from 0: '0,1,2,3...' The 'zero-eth' element of a string "Hello" is "H"; the first element of a list ['a', 'b', 'c'] is 'b'; and so on.*
- To run a Python program: ```$ python filename.py```

### PYTHON COMMENTS
- ```# some commment...```: *Any code after a ```#``` on the same line will not be read by the interpreter. Think of these as post-it notes for source-code, only you the programmer (and anyone inspecting the code) will see it. Useful for explaining each step of the program, putting in* ```#TODO...``` *notes for later when building a program, &c.*
- Any code in-between ```"""comment..."""``` will be read as a string literal, but since it isn't assigned to a variable it will simply be ignored. This is how you can 'cheat' multi-line comments.

## STRINGS (DATA STRUCTURE)
- *Strings are immutable, so to 'update a string' you must assign the string to a new one with the changes.*
  - ```string_name = "Some message"``` : *Strings can be in ```""``` or ```''```*
  - ```multiline_string = """Some message,```  
  ```continued on another line,```  
  ```continued on a third line."""```
  - ```string2 = string1 + "some text" + ...``` : *concatenating strings*
  
### STRING SLICE SYNTAX:
- **slice(start, stop, step)**: *Start & step are optional. The 'stop' means 'stop 1 before here' (non-inclusive). Step by -1 to reverse a string. Examples of s1="Hello":*
  - ```print(s1[::-1]``` ==> *olleH*
  - ```return s1[::2]``` ==> *Hlo*
  - ```s1[-1:]``` ==> *o*
  

  
- **f-strings**: *a way to include variables in strings. You can put any valid Python expression inside the {...} to evaluate at runtime.*
  - ```print(f"Hello, {name}.")``` ==> *Hello, David.*
  - ```return f"{name.lower()}"``` ==> *david*
  - ```f"Cost: {apples * 2.99}."```
  - ```print(f"{user[name]} is a {user[job]}.")``` ==> *David is a professor.*
  - ```print(f'{value:.2f}')``` ==> *3.23 (choose decimal place to round at)*

## LISTS (DATA STRUCTURE)
- *Lists are mutable, so you can change them without assigning them to a new list variable. Lists are ordered. Each element of a list can be an integer, a string, another list, &c.*
  - ```list_name.append(value)``` : *adds the value (string, int, another list) to the end of the list. (Note you don't have to set it ```=``` to a new list, as the old list can be updated, being mutable.)*
    - ```list.append(9)```: [1,5] => [1,5,9]
    - ```list.append([6,7]): [1,5] => [1,5,[6,7]]
  - ```list.extend(value)```: *extend adds iterable value to the list*
    - ```list.extend([6,7])```: [1,5] => [1,5,6,7]
    - ```list.extend('cdefg')```: ['a','b'] => ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  - ```for index, value in enumerate(list_name):``` : *loop thru a list, getting additional access to an index-number*



## DICTIONARIES
- *Dicts are mutable and unordered.*
  - ```dict_name = {}``` OR ```dict_name = dict()``` : *create an empty dict. You can also pre-populate the dict with {key:"value", key:"value"} pairs.*
  - ```dict_name[key] = value``` : *set a key/value pair, or update value of existing key*
  - ```print(dict_name.get(key))``` : *get dict value by key*
  - ```del dict_name(key)``` : *delete a dict key/pair*
  - ```for item in dict_name.items():``` : *loop thru dictionary, each 'item' is a (key,value) tuple*
  - ```for key, value in dict_name.items():``` : *Loop thru a dict, having access to key/value individually.*

## SETS
- *an unordered, unindexed (but mutable) collection of distinct objects; contained in '{}'. Since each value must be unique, common uses include membership testing, removing duplicates, &c.*
  - Create: ```demo_set = {'a', 'b', 'c'}``` OR ```demo_set = set(('a', 'b', 'c'))``` 
  - Access: *set items cannot be accessed by index or key, but you can loop through them to try and match an item (for-loop), or ask if a particular value is present (```for x in set:```)*
  - Add: ```demo_set.add('value')``` OR ```demo_set.update(['value1', value2', value3'])
  - Remove: ```demo_set.remove('value') 
  - Change: *you cannot change an existing set item (only delete, re-add updated item)*
  - Empty/Delete: ```demo_set.clear()``` / ```del demo_set```
  - Combine 2 sets: ```set3 = set1.union(set2)``` OR ```set1.update(set2)
  - Difference(): *returns a set containing the difference between 2+ sets*

## TUPLES



## FUNCTIONS
- def function_name(parameters): *a defined function says what will happen once it is atually called*
- a = fuction_name(parameter): *a function whose return value is outputted as 'a'*
   - ```a,b = function_name(parameters)```: *a function with multiple returns, outputted to 'a,b' in the same order. (Multiple outputs can be stored in 1 variable, but that it must be indexed to get out individual results.)*
- ```a, b = function(a)``` : *here function(a) returns (unseen) two variables. You can also return 2 variables to a single one, but then need to unpack/index it to access them.*

## CLASSES

## OPERATORS
- **Assignment Operators**
  - ```a = 10``` *the __Assignment Operator__. 'Declares' a variable's value (often a new variable).*
  - ```a += 10``` => ```a = a + 10``` *add a thing to itself ('updates' or refurbishes a variable)*
    - *See also:* ```-= , *= , /=, %=, //=, **= ``` *and more...*
- **Arithmetic Operators**
  - ```+, -, *, /, %, **, //```: *addition, subtraction, multiplication, division, modolus (divide and return the remainder), exponentiation, floor division (divide and return number w/0 the remainder).*
- **Comparison Operators**
  - ```x == y```: *checks for equality between the two– if x=10 and y=10, then x==y, so True.*
    - ```x != y```: *checks for non-equality between the variables– if x=10 and y=10, then False.*
  - ```x > y, x >= y, x < y, x <= y```: *x is greater than/greater than or equal to y, less than/less than or equal to.*
- **Logical Operators**
  - ```if x < 5 and x < 10```: *joins conditional statements– returns True if both/all statements are True.*
  - ```if x <5 or x > 10```: *returns True if just one of the statements is True.*
  - ```if not (x<5 and x<10)```: reverses the result– returns False if True, True if False.

## DECLARING VARIABLES
  - *Variables do not need explicit declarations of type, Python will interpret for you.*
- **Casting**: *changing the type of a variable, e.g. string '10' ==> int 10.*
    - *Check the type of a variable with ```print(type(variable))```*
  - ```int()```
  - ```str()```
- **Multiple Assignment**:
  - ```a = b = c = 10```: *multiple variables given the same single value*
  - ```a,b,c=1,2,"jen"```: *multiple variables given multiple objects, just on the same line*
- **Var: String**
  - ```name = "Cassady"```, ```num = '12543```` 
- **Var: Number**
  - **Integer**
    - ```counter = 1```
  - **Float**: *a float allows for decimal places*
  - ```miles = 100.05```
- **Var: Boolean**
  - ```switch = True```: *when declaring the value of a boolean variable, they must be capitalized (True/False).*
  - Boolean Rules: *any value that exists and returns a non-zero(+ or -) or non-empty value is True; 0 returns False. (Thus some variables, like strings, always return True as long as they aren't empty.)*

## MISCELLANEOUS
- **Ternary Operator**: ```value_if_true if condition else value_if_false```
  -  *consolidating multiple lines of code into one. ```If```s and ```else```s with only 1 line of code can skip the newline/indent; even simple for-loops can be reduced to one line*
  - ```return True if a > b else False```
  - ```if a > b: True``` , ```else: False```: *each conditional is on one line*
- **List Comprehension**: ```x = [expression for item in list]```
  - ```new_list = [letter for letter in 'some_string]```
- **Lambda f(x)**: *a small, anonymous function with exactly 1 expression (but any number of arguments/inputs)*
  - ```lambda arguments : expression```
    - ```x = lambda a : a + 10``` > ```print(x(5))```
- **Type Hinting**: *a form of program documentation (comments) that tell you what a function is expected to receive (parameters) and what it will output (return).*
  - ```def hello_name(name: str) -> str: return(f"Hello {name}.")```
  

## USEFUL FUNCTIONS:
- **range(start,stop,step)**: *start/step are optional. 'Stop' means it stop before that number (non-inclusive). Negative step number will go from the end to the beginning of the range.*
  -```for i in range(0,10,1):```
- **enumerate()**: *attaches an iterator (counter) to an object*
  -```for index, value in enumerate(list/string):```














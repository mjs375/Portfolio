# P Y T H O N  •  B A S I C S 
## TUTORIAL


### PYTHON COMMENTS
- Any code after a '\#' will not be read by the interpreter
- Any code in-between """...""" will be read as a string literal, but since it isn't assigned to a variable it will simply be ignored

## STRINGS (DATA STRUCTURE)
- *Strings are immutable, so to 'update a string' you must assign the string to a new one with the changes.*
  - ```string_name = "Some message"``` : *Strings can be in ".." or '..'*
  - ```multiline_string = """Some message,```  
  ```continued on another line,```  
  ```continued on a third line."""```
  - ```string2 = string1 + "some text" + ...```
  
- **Slice Notation**
  - 
- **f-strings**: *a way to include variables in strings. You can put any valid Python expression inside the {...} to evaluate at runtime.*
  - ```print(f"Hello, {name}.")``` ==> *Hello, David.*
  - ```return f"{name.lower()}"``` ==> *david*
  - ```f"Cost: {apples * 2.99}."```
  - ```print(f"{user[name]} is a {user[job]}.")``` ==> *David is a professor.*
  - ```print(f'{value:.2f}')``` ==> *3.23 (choose decimal place to round at)*

## LISTS (DATA STRUCTURE)
- *Lists are mutable, so you can change them without assigning them to a new list variable. Lists are ordered.*
  - ```list_name.append(value)``` : *adds the value (string, int, another list) to the end of the list.*
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
## TUPLES

## SLICE NOTATION:
- **slice(start, stop, step)**: *Start & step are optional. The 'stop' means 'stop 1 before here' (non-inclusive). Step by -1 to reverse a string. Examples of s1="Hello"*
  - ```print(s1[::-1]``` ==> *olleH*
  - ```return s1[::2]``` ==> *Hlo*
  - ```s1[-1:]``` ==> *o*
  


## FUNCTIONS
- def function_name(parameters):

## CLASSES

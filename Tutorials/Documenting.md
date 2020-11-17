# Commenting and Documenting Code

## Commenting
- *Code tells you how; comments tell you why.*
```python
def hello_world():
  # A simple comment remarking on a function (max 72 char)
  print("Hello world")
```  
- Comments are good for:
  - planning and reviewing: ```# Step 1 here```, ```# Step 2 here```...
  - code description: ```# prompt user for new settings```
  - algorithmic description: ```# a quick-sort algorithm (performance gains)```
  - tagging: ```TODO: add condition for when val is None```
  

- **Type Hinting**: *a form of program documentation (comments) that tell you what a function is expected to receive (parameters) and what it will output (return).*
  - ```def hello_name(name: str) -> str: return(f"Hello {name}.")```
  
## Docstrings 
- *an important key to documenting your program that help user's understand the code.*
  - ```help(str)```: *a built-in Python function that prints out an object's docstring to the console.* ```$ python3``` => ```>>>help(str)``` => ```Help on class str in module builtins. class str(object): Create a new string object ...```
  - ```>>> dir(str)```: *examine the directory of an object using ```dir()```. Within this list is one interesting one, ```__doc__``.*
  - ```>>> print(str.__doc__)``` => ```Create a new string object from a given object...```
  - **Set a docstring**:
```python
def say_hello(name):
  print(f"Hello, {name}.")
say_hello.__doc__ = "A simple function that says hello."
```
=>
```bash
$ python3
>>> help(say_hello)
Help on function say_hello in module __main__:
   say_hello(name)
     A simple function that says hello.
```
- Docstrings should either be 1 line (short and summarizing), or follow a multi-line standard:
```python
"""Summary line

This is further elaboration of the docstring. Go into
details as appropriate... Notice that the summary and description
are separated by a line.
"""

# code continues after a one-line break
```


### Class Docstrings
- Docstrings can be created for the ```class``` itself, as well as any ```class methods```.
  - **Class Docstring**: summarize purpose and behavior of class, list any public methods and class proprties, and anything related to sub-classes
```pytohn
class SampleClass:
  """Class docstring here."""
  
  def say_hello(self, name: str):
    """Class-method docstring goes here."""
    
    print(f"Hello {name}.")
```
- An extensive example of a fully-documented ```class```:
```python
class Animal:
  """
  A class used to represent an Animal.
  
  ...
  Attributes
  ----------
  says_str : str
    a formatted string to print out what the animal says
  name : str
    the name of the animal
  sound : str
    the sound the animal makes
  num_legs : int
    the number of legs the animal has (default 4)
  
  Methods
  -------
  says(sound=None)
    Prints out the animals name and what sound it makes
  """
  
  says_str = "A {name} says {sound}
  
  def __init__(self, name, sound, num_legs=4):
    """
    Parameters 
    ----------
    name : str
      The name of the animal
    sound : str
      The sound the animal makes
    num_legs : int, optional
      The number of legs the animal has (default = 4)
    """
    
  def says(self, sound=None):
    """Prints out what the animals name is and what sound it makes.
    
    If the argument 'sound' isn't passed in, the default Animal sound is used
    
    Parameters 
    ----------
    sound : str, optional
      The sound the animal makes (default is None)
    
    Raises
    ------
    NotImplementedError
      If no sound is set for the animal or passed in as a parameter.
    """
    
    if self.sound is None and sound is None:
      raise NotImplementedError("Silent Animals are not supported")
    
    out_sound = self.sound if sound is None else sound
    print(self.says_str.format(name=self.name, sound=out_sound))
````
















[Source](https://realpython.com/documenting-python-code/#why-documenting-your-code-is-so-important)

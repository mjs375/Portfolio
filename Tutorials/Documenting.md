# Commenting and Documenting Code

- **Type Hinting**: *a form of program documentation (comments) that tell you what a function is expected to receive (parameters) and what it will output (return).*
  - ```def hello_name(name: str) -> str: return(f"Hello {name}.")```
- **Docstrings**: *an important key to documenting your program that help user's understand the code.*
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
```
$ python3
>>> help(say_hello)
Help on function say_hello in module __main__:
   say_hello(name)
     A simple function that says hello.
```




[Source](https://realpython.com/documenting-python-code/#why-documenting-your-code-is-so-important)

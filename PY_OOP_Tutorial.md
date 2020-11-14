# Object-Oriented Programming (OOP)

### Programming Paradigms
- **Object-Oriented:** *structuring of programs so that properties and behaviors are bundled into individual __objects__. Objects are the center of OOP, not just in representing data, but the overall structure of the program.*
  - **Object:** *represents an entity with __properties__, e.g. a Person with a Name, Age, Address, and __behaviors__ (like walking, speaking); or an Email, with properties such as a Recipient List, Subject, Body, and behaviors like adding attachments and ending.*
- **Procedural/Functional:** *structures a program like a recipe, i.e. a series of steps in the form of functions and code blocks, which flow sequentially to complete a task.*


### Classes
- **Primitive Data Structures**: *represent simple pieces of information, e.g. strings, integers, lists.*
  - **Example List:** ```kirk, spock  = ["James Kirk", 34, "Captain", 2256], ["Spock", 35, 2254]
    - **Flaws:** *difficult to manage, remembering just what kirk[#] exactly is, errors if all employees don't have the same number of elements in a list...*
- **Classes:** *used to create user-defined data structures.*
  - **Methods:** *class-defined functions, which ID behaviors and actions that an object can perform with its data.*
  - **Class vs. Instance:** *the Class is the blueprint, the 'idea' of a dog (that a Dog has a name, age, breed); an Instance is one actual Dog (Spot, age 3, dalmatian).*

#### Defining a Class
- **Properties:** ```__init__()``` *method defines all properties that an object of its class must have. Everytime an Object of a Class is initialized, ```__init__()``` sets initial states for the object by assigning values (any number of parameters, but the first is always ```self```, which helps define attributes on itself).*
- **Instance Attributes:** *created in ```__init__()```, and are particular to each particular object instance (one dog is named Spot, another Grover).*
- **Class Attributes:** *attributes that have the same value for all instances of the class. Define them by assigning a value to a variable outside of ```__init__()``` (below the class definition). They must always have an initial value, as all instances of the class are automatically assigned these values.*
```python
class PetDog: # name classes in this way: class ClassName
  species = "Canis familiaris" # class attribute (value same in all objects of class Dog)
  def __init__(self, name, age): # method, creating attributes
    self.name = name # creates 'name' attribute, assigns it to the value of the 'name' parameter
    self.age = age # instance attribute (value particular in each class Dog instance)
```

#### Instantiating a Class Object
- **Creating a New Object:** ```Dog()``` => *creating an instance is called __instantiation__. Type the name of the class like this: Class(). Each instance is totally unique and stored in a different memory address (even 2 instances like 'a=Dog()' and 'b=Dog()', which are both 'empty' of attributes because in this case there are no attributes inside 'Dog')*
- **Providing Values:** *you need to provide values for each instance attribute, or else you will encounter a ```TypeError```.*
```python
cassie = Dog('Cassie', 12) # creates an instance of Dog 
eli = Dog('Eli', 3) 
```
- **Access Attributes:** *use __dot notation__ to access a particular attribute of any object (a class attribute or an instance attribute).*
  - ```cassie.age``` => ```12```
  - ```eli.species``` => ```Canis familiaris```
- **Changing an Object's Attributes:** *attributes are guaranteed to exist for each instance of a class object. But, you can still change them. Objects are __mutable__!*
  - ```cassie.age = 13 #`changed from '12'```

#### Instance Methods
- *__Instance methods__ are functions that are defined inside a class and can only be called from an instance of that class. Just like ```__init__(self, a, b)```, an instance method's first parameter is always ```self```.*
  - *A common and useful instance method is to have something which returns a a 'description' of that instance/object.*
    - ```print(miles)``` => ```<__main__.Dog object at 0x00aeff70>``` *(non-useful memory address)*
    - ```print(miles)``` => ```'Miles is 4 years old'``` *(output IF \__str__ is set)*
 - **Dunder Methods:** *these methods begin and end with double underscores(\__), like ```__init__()``` and ```__str__()```, and are special.*
    
```python
class Dog
  species = "Canis familiaris" # a class attribute (all have same value, auto-provided)
  # Creating instance attributes (each instance gets a unique value):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Instance method:
  def __str__(self): # returns a string descriptor
    return f"{self.name} is {self.age} years old."
  # another instance method
  def speak(self, sound): # has 1 parameter 'sound', returns a string...
    return f"{self.name} says {sound}."
#
#
miles = Dog('miles', 4) # instantiate an object of class Dog
miles.description() # => 'Miles is 4 years old'
miles.speak('Woof Woof!') # => 'Miles says Woof Woof!'
miles.speak('Bow wow') # => 'Miles says Bow wow'
```


### Inheritance
- *when one class takes on the attributes and methods of another (child derives from parent).*
  - **Parent classes** => **Child classes**
- **Child classes:** *inherit all the attributes/methods of the parent, but can override or extend them in a way unique to themselves.*
  - **Create a Child Class:** ```class ShetlandSheepdog(Dog): pass``` => ```class ChildClass(ParentClass): pass``` *(the 'pass' because here you're simply inheriting the attributes/methods of class 'Dog')*
    - *E.g. as a child of your parent, you inherit the attribute 'hair color'– but you can override the value itself if you have brown-hair and she is blonde. Perhaps you also learn a 2nd language in addition to your mothertongue in primary school– in this case you've extended the 'language attribute'.*
- **type(obj)**: *determine which class an object belongs to*
  - ```type(eli)``` => ```<class '__main__.BorderCollie'>```
- **isinstance(obj, class)**: *determine if an object is an instance of a particular class (returns True or False)*
  - *e.g. Cassie & Eli are both instances of the 'Dog' parent-class, but not equivalent in child-class type.*
```python
class Dog # PARENT CLASS
  species = "Canis familiaris"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} is {self.age} years old"
  def speak(self, sound):
    return f"{self.name} says {sound}"

class ShetlandSheepdog(Dog): # CHILD CLASS (inherits from 'Dog')
  pass # simply inheriting attributes/methods of parent-class Dog

class BorderCollie(Dog):
  pass

# Instantiate some child-class dogs
cassie = ShetlandSheepdog('Cassie', 10)
eli = BorderCollie('Eli', 3)

# Test inheritance
print(cassie.species) # => 'Canis familiaris'
print(eli.name) # => 'Eli'
print(eli.speak('Woof')) # => 'Eli says Woof'
```






[Source](https://realpython.com/python3-object-oriented-programming/)

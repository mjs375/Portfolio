


### Imports
```python
from time import sleep 
  #--control length of pin pulses (on/off, high/low)
import sys
  #--
import RPi.GPIO
  #--control Raspberry PI GPIO pins
import math # math.sqrt
  #--Calc'ing the belt lengths using PythagTheorem
import time
  #--Timing programs/stalling programs...

```
### Classes
```python
"""
Origin => (0,0) # top-left corner
X-axis is positive to the right,
Y-axis is positive downwards
  
"""


class Plotter:
  """
  class Plotter
  
  Attributes:
  -
  -
  Methods:
  -
  -
  """
  def __init__(self, width, height, **kwargs):
    #--
    self.width = width 
    #--
    self.height = height
    #--Initialize the pen position (which will change):
    self.position = kwargs.pop(...)
    #--Save the start position:
    self.initial = kwargs.pop(...)
    
  #
  def calc_belt_length(self, position):
    
    
    
```





```python
class Point:
  def __init__(self, x, y, c):
    self.x = x                  #--Horizontal coordinate
    self.y = y                  #--Vertical coordinate
    self.z = z or 1             #--1 if pen-up, 0 if pen-down
    self.c = 'blk' or c         #--Point color
  def __str__(self):
    return f"{self.x},{self.y},{self.z} (self.c)."

```

















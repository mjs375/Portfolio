


### Imports
```python
from time import sleep 
  #--control length of pin pulses (on/off, high/low)
import sys
  #--
import RPi.GPIO
  #--control Raspberry PI GPIO pins

```
### Classes
```python
class Plotter(self, ):
  def __init__(self, ):
    self. = 
    self. = 
```
```python
class Point(self, x, y, z, color):
  def __init__(self, x, y, color):
    self.x = x                  #--Horizontal coordinate
    self.y = y                  #--Vertical coordinate
    self.z = z or 1             #--1 if pen-up, 0 if pen-down
    self.color = 'blk' or color #--Point color
  def __str__(self):
    return f"{self.x},{self.y},{self.z} (self.color)."

```

















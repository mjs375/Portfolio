"""
Origin => (0,0) # top-left corner
X-axis is positive to the right,
Y-axis is positive downwards
  
"""


class Weaver:
  """
  class Weaver – a single drawing instance. Moves belts to align pen-gondola with a point in the drawing-area.
  
  Attributes:
  -
  -
  Methods:
  -
  -
  """
  def __init__(self, width, height, **kwargs):
    #--Distance between L/R motors (width of drawing area):
    self.width = width 
    #--Distance to bottom of drawing area:
    self.height = height
    #--Initialize the pen position to center of wall (which will change):
    self.position = kwargs.pop('initial_position', [width/2, height/2])
    #--Save the starting position:
    self.initial_position = kwargs.pop('initial_position', [width/2, height/2])
    #
    #--Set pen speed
    self.speed = 
    #--
    
  #
  #
  #
  def _calc_belt_length(self, position): # (method starts w/ '_' to indicate it is for internal use only)
    """ Calculates the length of each belt based on its current or expected position. {c = sqrt(a**2 + b**2) / self.position = width, height (x,y).}"""
    #-- left belt = sqrt(width**2, height**2)
    left_belt = math.sqrt(position[0]**2 + position[1]**2)
    #--
    right_belt = 
    return left_belt, right_belt
  #
  #
  #
  def move(self, next_position):
    """ Move pen-gondola to new position """
    #--Calc delta of belt lengths (start position & next position):
    start_lengths = self._calc_belt_lengths(self.position)
    stop_lengths =  self._calc_belt_lengths(next.position
    #--Calc motor movement to reach new lengths (new position):
    left_steps =
    right_steps =
    #--Calc duration based on move length & speed:
    duration = 
    #--Move the motors:
    self.spin
    #--Sleep so commands don't stack
    time.sleep(duration/1000)
    
class Point:
  def __init__(self, x, y, c):
    self.x = x                  #--Horizontal coordinate
    self.y = y                  #--Vertical coordinate
    self.z = z or 1             #--1 if pen-up, 0 if pen-down
    self.c = 'blk' or c         #--Point color
  def __str__(self):
    return f"{self.x},{self.y},{self.z} (self.c)."

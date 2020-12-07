


### Imports
```python
  #IMPORTS
from time import sleep 
  #--control length of pin pulses (on/off, high/low)
import sys
  #--
import RPi.GPIO
  #--control Raspberry PI GPIO pins


#### Demo
```
- **Sample example, toggles an output pin on/off for 200ms x10.
```python
import RPi.GPIO as GPIO
import time

LED = 18
switch = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)

for i in range(10):
  GPIO.output(LED, GPIO.HIGH)
  time.sleep(0.2)
  GPIO.output(LED, GPIO.LOW)
  time.sleep(0.2)
  print("Switch states = ", GPIO.input(switch))

GPIO.cleanup()

```


















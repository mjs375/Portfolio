# Mathematics of Plotting

### Calculating Belt Length
- **Pythagoras' Theorem**: ```a² + b² = c²```, ```c = √{a² + b²}```
  - B<sub>L</sub> = ``` √{(x)² + (h-y)²}```
  - B<sub>R</sub> = ``` √{(w-x)² + (h-y)²}```

### Shortest Distance between Points
- How can we minimize redundant travel-time between the ends of lines and the starts of the next lines?
  - Travelling Salesman Problem! use ```mlrose``` to solve for shortest travel distance between nodes.
- Many Pen Plotters use a __greedy approach__: they simply find the next-nearest undrawn point after finishing one line/path (iterative).
  - Remember, when the 'pen is down', we will always travel the same distance: the lines we need to draw. We need to minimize the travel-time when the 'pen is up'.

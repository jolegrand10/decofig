# Decofig
This is decofig's read me file.

An example of usage of the Decorator design pattern with geometrical figures in Python.

It uses the turtle library to draw the figures.

## Abstract figure
The abstract figure is defined in figure.py by the class `Figure`. Its attributes are a list of points and a dict of properties.

### Prop
- `backgroundColor`
- `closed` True, to add a line that connects the last point to the first one (to close the figure)
- `lineColor`
- `lineWidth`
- `showTurtle`
### Methods
The Figure class provides public methods:
- `str` gives a text inventory of the content of a figure, made of points and properties
- `repr` gives a text representing a Python expression that will recreate the figure, when evaluated
- `len` gives the number of points, nodes of the figure
- `draw`  draws the figure using the turtle library
- `translate` and `rotate` are isometries

## Concrete figures
Concrete figures are Dot, Line, Polyline, Polygon, Rectangle, Rhombus

## Abstract decorator
The abstract decorator is defined in figuredecorator.py by the class FigureDecorator. 

## Concrete decorators
Concrete decorators have names starting with "with" :
- `WithDots` shows a small diskshape at the beginning and the end of each line segment
- `WithCentre` shows a small diskshape at the center of gravity of a figure
- `WithTransparency` suppresses the filling color of a figure

The following are isometries,ie transformations that preserve figure's shape, size, aspect, internal distances and angles
- `WithRotation`, rotates the figure around its centre of gravity
- `WithTranslation` moves the figure to another position

### WithDots
#### Added props
- `dotColor`
- `dotSize`


### WithCentre
#### Added props
- `centreSize`
- `centreColor`

### WithTransparency
#### Added props
- None.
Modifies the background color only.
### WithTranslation
#### Added props
- None.
Modifies points only.
### WithRotation
#### Added props
- None.
Modifies points only.
## About this branch
Branch is named "master"
The option in this branch is 
- to `__repr__` a figure in a way that reflects properly the current figure but not the actual
instantiations that led to this result.
- to `deepcopy` the starting figure in the decoration process so that the decoration process does not alter
the original figure. The original figure survives unchanged and may be safely reused.


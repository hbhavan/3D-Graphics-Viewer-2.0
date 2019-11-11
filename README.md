# 3D-Graphics-Viewer-2.0
Python implementation of my 3D graphics viewer with user controls

This program takes in a text file that contains the endpoints of lines
in 3D space and displays them on the screen in 2D space. The format of
a line in the text file is as such:
  x0 y0 z0 x1 y1 z1
  
The example text file 'house.txt' is included. It is a cube centered at
the origin with a square pyramid on top. 

Objects in 3D space can be:
  Translated in the x, y, and z direction
  Rotated about the x, y, and z axis
  Scaled up or down
These transformations can be applied by pressing a key on the keyboard.
The speciifc keybinds are listed when the program is ran.

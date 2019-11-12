# 3D-Graphics-Viewer-2.0
Python implementation of my 3D graphics viewer with user controls

This program takes in a text file that contains the endpoints of lines
in 3D space and displays them on the screen in 2D space. The text file
is formated as such:
  All the points that make up an object in 3D space are listed in the
  text file. Each line contains the x, y, and z coordinates as floats.
  After all the points, enter a '~' on its own line.
  Then, list which points make up the endpoints of a line using the
  index of those points in the text file.
    Ex: x0 y0 z0
        x1 y1 z1
        x2 y2 z2
        ~
        0 1
        0 2
        1 2
    
The example text file 'house.txt' is included. It is a cube centered at
the origin with a square pyramid on top. 

Objects in 3D space can be:
  Translated in the x, y, and z direction
  Rotated about the x, y, and z axis
  Scaled up or down
These transformations can be applied by pressing a key on the keyboard.
The speciifc keybinds are listed when the program is ran.

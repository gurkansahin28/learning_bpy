##########################################################################
import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *

import math
import numpy

r=5
width=0.2
z=0

for x in numpy.arange(0.0, r+1, 0.1):
    y=math.sqrt((r*r)-(x*x))
    print("the value of x and y", x, y)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z), size=width)
    bpy.ops.mesh.primitive_cube_add(location=(-x, y, z), size=width)
    bpy.ops.mesh.primitive_cube_add(location=(-x, -y, z), size=width)
    bpy.ops.mesh.primitive_cube_add(location=(x, -y, z), size=width)

##########################################################################

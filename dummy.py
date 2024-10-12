# https://docs.blender.org/api/current/index.html
################################################################
# Checking the Python release
>>> import sys
>>> sys.version
###############################################################
# Checking the Blender release in the Python script
>>> import bpy
>>> bpy.app.version
###############################################################
# Achieving bpy.app.version data in detail
>>> major, minor, micro = bpy.app.version
>>> print("Major version:", major)
>>> print("Minor version:", minor)
>>> print("Micro version:", micro)
################################################################
import bpy

print("Hello from Blender!")

for i, ob in enumerate(bpy.data.objects):
  print(i, ob.name, ob.type)

###############################################################
# Header for Blender Scripting files
import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
################################################################

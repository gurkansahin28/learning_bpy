##########################################################################

import bpy

# Create cubes in Blender and scale them according to the Fibonacci sequence

fibs = [] # empty list
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
fibCount = 10

# Make and populate the list of Fibonacci numbers

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(fibCount):
    fibs.append(fib(i))

# Create cubes according to the Fibonacci sequence
# Location and size of the cubes  corresponed to the Fibonacci sequence

for i in range(len(fibs)):    
    bpy.ops.mesh.primitive_cube_add(location=(fibs[i], fibs[i], fibs[i]), size = fibs[i])
    
##########################################################################

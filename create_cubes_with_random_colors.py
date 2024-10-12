#################################################################################
#
import bpy
import random

cubes = 10

for i in range(cubes):
    bpy.ops.mesh.primitive_cube_add(location=(i+i*0.2, 0, 0), size = 1)
    # Make new material :
    mat = bpy.data.materials.new("Material" + str(i))
    # make random color diffuse :
    mat.diffuse_color = (random.random(), random.random(), random.random(), 1)    
    # Assign material to object
    bpy.context.object.data.materials.append(mat)
#################################################################################
#

#################################################################################

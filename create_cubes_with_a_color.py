##########################################################################
import bpy

cubes = 10
sceneCubes = []

# Create new Yellow Material
YELLOWMat = bpy.data.materials.new("YELLOW_Material")
YELLOWMat.diffuse_color = (255, 255, 0, 1)


# Create Cubes
for i in range(cubes):
    bpy.ops.mesh.primitive_cube_add(location=(i+i*0.2, 0, 0), size = 1)
    bpy.context.object.name = "Cube" + str(i)
    # Add cube reference to list
    sceneCubes.append("Cube" + str(i))
    

# Deselect Eveything to have a clean slate  
bpy.ops.object.select_all(action='DESELECT')


# Select every other cube from the list
for i in range(len(sceneCubes)):
    if i % 2 == 0:
        bpy.ops.object.select_pattern(pattern=sceneCubes[i])              

# Define selected cubes:
selectedCubes = bpy.context.selected_objects

# Assign Material to selected cubes:
for cube in selectedCubes:
    cube.data.materials.append(YELLOWMat)
##############################################################################

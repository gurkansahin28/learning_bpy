################################################################
import bpy

print("Hello from Blender!")

for i, ob in enumerate(bpy.data.objects):
  print(i, ob.name, ob.type)

###############################################################

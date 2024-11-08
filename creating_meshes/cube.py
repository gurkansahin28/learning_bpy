#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:42:40 2024

@author: gurkan
"""

import bpy

# Create a cube and name it "MyCube"
bom = bpy.ops.mesh
bom.primitive_cube_add(size=2)
cube = bpy.context.object
cube.name = 'MyCube'
cube.location = (2, 2, 0)
cube.rotation_euler = (1.0, 0.5, 0.0)
bpy.data.objects['MyCube'].location = (-2, -1, 0)
bpy.context.view_layer.update()

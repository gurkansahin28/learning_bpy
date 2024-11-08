#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:42:40 2024

@author: gurkan
"""

import bpy

# Create a sphere and name it "MySphere"
bom = bpy.ops.mesh
bom.primitive_uv_sphere_add(radius=1)
sphere = bpy.context.object
sphere.name = "MySphere"  # Assign a specific name to the sphere
sphere.location = (0, 0, 0)
sphere.rotation_euler = (1.0, 0.3, 0.2)
MySphere = bpy.data.objects['MySphere']
MySphere.location = (2, 2, 0)


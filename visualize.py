# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 23:54:09 2018

@author: pabre
"""

y0=10
image="viu-la-vida.png"
forme="spheres" #spheres ou cubes

import csv
import bpy

inpath="C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\"
filein=str(inpath)+str(forme)+'_'+str(image.rsplit('.')[0])+'_'+str(y0)+'.csv'
csv.reader(open(filein))
for line in filein:
    if forme == 'cubes':
        bpy.ops.mesh.primitive_cube_add(radius=float(line[3])/2.,location=(float(line[0]),float(line[1]),float(line[2])))
    else:
        bpy.ops.mesh.primitive_uv_sphere_add(size=float(line[3])/2.,location=(float(line[0]),float(line[2]),float(line[3])/2.))
#import bpy
import csv
#file = csv.reader(open("C:\Users\pabre\Desktop\Documents\question_dangle\list_cubes2.txt"))
file = csv.reader(open("C:\\Users\\pabre\\Desktop\\Documents\\question_dangle\\list_cubes.csv"))
#file=open("C:\\Users\\pabre\\Desktop\\Documents\\question_dangle\\list_cubes.txt")
for line in file:
    x=line[0]
    y=line[1]
    z=line[2]
    p=line[3]
    bpy.ops.mesh.primitive_cube_add(radius=float(p), location=(float(x),float(y),float(z)))

#file.close


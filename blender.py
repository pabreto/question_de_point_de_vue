#import bpy
from PIL import Image
from random import randint
import numpy as np

y0=10 #Distance observateur/premiere couche de l'image (cm)
#image="visage.png"  #image a dessiner
#image="cercle_barre.png"  #image a dessiner
#image="trait_horizontal.png"  #image a dessiner
#image="trait_vertical.png"  #image a dessiner
#image="croix.png"
#image="bonjour.png"
#image="question_de_point_vue0.png"
#image="image.png"
image="viu-la-vida.png"
forme="spheres" #spheres ou cubes
p0=1 #taille du "pixel" sur la premiere couche de l'image (cm) #rayon apparent
factor=2 #facteur d'agrandissement max de l'image (ymax/y0)

#load the pic
im = Image.open(image) #Can be many different formats. 
pix = im.load() #trouve la couleur du pixel
size_x=im.size[0] #Get the width and hight of the image for iterating over
size_z=im.size[1]
print('size_x =',size_x)
print('size_z=',size_z)


file_out_name=str(forme)+'_'+str(image.rsplit('.')[0])+'_'+str(y0)+'.csv'
file_out=open(file_out_name,"w") #-%s-%i ,%image,%y0

#r=1 #taille du pixel en bas a gauche/taille du pixel original	l
a=[[0,0,0,0],[0,0,0,0]] #on initialise a avec deux lignes pour ne pas avoir de problemes de dimension dans la boucle

size=1
#parcourt pixel de l'image reelle
for x0 in range(0,size_x):
    for z0 in range(0,size_z): #si pixel non blanc
        if pix[x0,z0] != (255,255,255,255):
            #r=randint(1,10)#
            r=randint(100, 100*factor)/100. #r=facteur de reduction aleatoire (entre 100 et 300% de la taille du pixel de base)
            p=float(r)*p0			
            x=r*(x0-float(size_x)/2)
            z=-r*(z0-float(size_z)/2)
            y=r*y0-p
            new_a=[x,y,z,p]
            for s in range (1,size):
                d=np.sqrt( (x-(a[s])[0])**2+ (y-(a[s])[1])**2 + (z-(a[s])[2])**2 )
                if forme == 'cubes':
                    dmin=np.sqrt(2)*(r+(a[s])[3])
                else:
                    dmin=r+(a[s])[3]
                if float(d) < dmin:
                    break
                else :
                    continue
            a=np.vstack([a,new_a])
            size=size+1


print('a=',a)
print(size)
for i in range (1,size+1):
	file_out.write(str((a[i])[0])+','+str((a[i])[1])+','+str((a[i])[2])+','+str((a[i])[3])+'\n')
file_out.close

#Script to visualize
#~ 
#y0=10
#image="viu-la-vida.png"
#forme="spheres" #spheres ou cubes

#import csv
#import bpy

#inpath="C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\"
#filein=str(inpath)+str(forme)+'_'+str(image.rsplit('.')[0])+'_'+str(y0)+'.csv'
#csv.reader(open(filein))
#for line in filein:
#    if forme == 'cubes':
#        bpy.ops.mesh.primitive_cube_add(radius=float(line[3])/2.,location=(float(line[0]),float(line[1]),float(line[2])))
#    else:
#        bpy.ops.mesh.primitive_uv_sphere_add(size=float(line[3])/2.,location=(float(line[0]),float(line[2]),float(line[3])/2.))


#Script to print
#~ 
#y0=10
#image="viu-la-vida.png"
#forme="spheres" #spheres ou cubes

#import csv
#import bpy

#inpath="C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\"
#filein=str(inpath)+str(forme)+'_'+str(image.rsplit('.')[0])+'_'+str(y0)+'.csv'
#csv.reader(open(filein))
#for line in filein:
#    if forme == 'cubes':
#        bpy.ops.mesh.primitive_cube_add(radius=float(line[3])/2.,location=(float(line[0]),float(line[2]),float(line[3])))
#    else:
#        bpy.ops.mesh.primitive_uv_sphere_add(size=float(line[3])/2.,location=(float(line[0]),float(line[2]),float(line[3])/2.))
#    bpy.ops.object.select_all(action='SELECT')
#   fPath = str(("C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\spheres.stl"))
#  bpy.ops.export_mesh.stl(filepath=fPath)
    

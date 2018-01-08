#import bpy
from PIL import Image
from random import randint
import numpy as np

y0=50 #Distance observateur/premiere couche de l'image (cm)
#image="visage.png"  #image a dessiner
#image="cercle_barre.png"  #image a dessiner
#image="trait_horizontal.png"  #image a dessiner
#image="trait_vertical.png"  #image a dessiner
#image="croix.png"
#image="bonjour.png"
#image="question_de_point_vue0.png"
#image="image.png"
image="viu-la-vida.png"

p0=1 #taille du "pixel" sur la premiere couche de l'image (cm) #rayon apparent


#load the pic
im = Image.open(image) #Can be many different formats. 
pix = im.load() #trouve la couleur du pixel
size_x=im.size[0] #Get the width and hight of the image for iterating over
size_z=im.size[1]
#print('size_x =',size_x)
#print('size_z=',size_z)

#file_out=open("list_cubes.csv","w")
file_out=open("list_spheres.csv","w")
#r=1 #taille du pixel en bas a gauche/taille du pixel original	l
a=[[0,0,0,0],[0,0,0,0]] #on initialise a avec deux lignes pour ne pas avoir de problemes de dimension dans la boucle

size=1
#parcourt pixel de l'image reelle
for x0 in range(0,size_x):
    for z0 in range(0,size_z): #si pixel non blanc
        if pix[x0,z0] != (255,255,255,255):
            #r=1
            #r=randint(1,10)#
            r=randint(100, 300)/100. #r=facteur de reduction aleatoire (entre 100 et 300% de la taille du pixel de base)
            p=float(r)*p0			
            x=r*(x0-float(size_x)/2)
            z=-r*(z0-float(size_z)/2)
            y=r*y0-p
            new_a=[x,y,z,p]
            for s in range (1,size):
                d=np.sqrt( (x-(a[s])[0])**2+ (y-(a[s])[1])**2 + (z-(a[s])[2])**2 )
  #              if float(d) < np.sqrt(2)*(r+(a[s])[3]): #if yes, cubes are intersecting then break
                if float(d) < r+(a[s])[3]: #if yes, spheres are intersecting then break
                   # print('ca touche')
                    break
                else :
                    continue
          #  print('point',x0-float(size_x)/2,y0,z0-float(size_z)/2)
          #  print('transformé en ',new_a)
            a=np.vstack([a,new_a])
            size=size+1


print('a=',a)
#print(size)
for i in range (1,size+1):
	file_out.write(str((a[i])[0])+','+str((a[i])[1])+','+str((a[i])[2])+','+str((a[i])[3])+'\n')
file_out.close
#~ 
#~ script blender :
#~ import csv
#~ file=csv.reader(open("/home/localuser/Bureau/perspective/list_cubes.csv"))
#file=csv.reader(open("C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\list_cubes_trait.csv"))
#file=csv.reader(open("C:\\Users\\pabre\\Desktop\\Documents\\question_de_point_de_vue\\list_cubes_trait.csv"))
#~ for line in file:
  #  bpy.ops.mesh.primitive_uv_sphere_add(size=float(line[3])/2,location=(float(line[0]),float(line[1]),float(line[2])))

	#~ bpy.ops.mesh.primitive_cube_add(radius=float(line[3])/2,location=(float(line[0]),float(line[1]),float(line[2])))
#~ 

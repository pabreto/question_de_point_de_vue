#import bpy
from PIL import Image
from random import randint
import numpy as np

y0=200 #Distance observateur/première couche de l'image (cm)
#image="image.png"  #image à dessiner
#image="cercle_barre.png"  #image à dessiner
image="cercle.png"  #image à dessiner

p0=2 #taille du "pixel" sur la première couche de l'image (cm)


#load the pic
im = Image.open(image) #Can be many different formats.
pix = im.load()
size_x=im.size[0] #Get the width and hight of the image for iterating over
size_z=im.size[1]
print(size_x)
print(size_z)

#file_out=open("list_cubes.csv","w")
#file_out=open("list_cubes_cercle_barre.csv","w")
file_out=open("list_cubes_cercle.csv","w")
r=1 #taille du pixel en bas à gauche/taille du pixel original
k=1 #increment en pourcentage d'augmentation de la taille des pixels
for x0 in range(1,size_x):
    for z0 in range(1,size_z):
        #si pixel non blanc
        if pix[x0,z0] != (255,255,255):
            flag=1
#            print "Pixel at position",x,z,"is black"
            p=r*p0
#            print "taille nouveau pixel=",p
            x=r*x0
            z=r*z0
            y=r*y0
            a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
            for i in range(len(a)):
                for j in range(len(a[i])):
                    print(a[i][j], end=' ')
                print()
            
#            a=[[x,y,z,p]]
            while ( flag != 0 ) :
                r=randint(100, 300)/100. #r=facteur de reduction aleatoire (entre 100 et 300% de la taille du pixel de base)
				#            print "rapport taille pixel=",r
                #shape_a=a.shape
                #print(shape_a[0]-1)
                len=len(a) #/3-1
                for s in range(len):
#☺                for s in range(0,5):
                    print(a[0][2])
                    d=np.sqrt((x-a[0][s])**2+(y-a[1][s])**2+(z-a[2][s])**2)
				#loop on all points that have been placed to check if the distance between the new point and the points before is inferior to the sum of the diameter of the 2 cubes
                    if d < r+a(3,s):
                        #if yes, cubes are intersecting, leave and chose new r
                        break
                    else:
                        #else, append point to array and change flag
                        a=np.append(a,[x,y,z,p])
                        flag=0
                        print("Original position: (",x0,", 0,",z0,") - size: ",p0,"cm")
                        print("New position: (",x,",",y,",",z,") - size: ",p,"cm")
                        file_out.write(str(x)+","+str(y)+","+ str(z)+","+str(p)+'\n')
#						bpy.ops.mesh.primitive_cube_add(radius=p, location=(x,y,z))
#            file_out.write("("+str(x)+", "+str(y)+", "+ str(z)+")"+'\n')

file_out.close
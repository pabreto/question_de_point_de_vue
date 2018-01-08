#import bpy
from PIL import Image
from random import randint

y0=20 #Distance observateur/première couche de l'image (cm)
#image="image.png"  #image à dessiner
#image="cercle_barre.png"  #image à dessiner
image="cercle.png"  #image à dessiner

p0=2 #taille du "pixel" sur la première couche de l'image (cm)


#load the pic
im = Image.open(image) #Can be many different formats.
pix = im.load()
size_x=im.size[0] #Get the width and hight of the image for iterating over
size_z=im.size[1]
print size_x
print size_z

#file_out=open("list_cubes.csv","w")
#file_out=open("list_cubes_cercle_barre.csv","w")
file_out=open("list_cubes_rectangle.csv","w")

for x0 in range(1,10):
    for z0 in range(1,10):
        #si pixel non blanc
#        if pix[x0,z0] != (255,255,255):
#            print "Pixel at position",x,z,"is black"
        r=randint(50, 200)/100. #r=facteur de reduction aleatoire (entre 50 et 200% de la taille du pixel de base)
#            print "rapport taille pixel=",r
        p=p0*r
#            print "taille nouveau pixel=",p
        x=r*x0
        z=r*z0
        y=r*y0
        print "Original position: (",x0,", 0,",z0,") - size: ",p0,"cm"
        print "New position: (",x,",",y,",",z,") - size: ",p,"cm"
        file_out.write(str(x)+","+str(y)+","+ str(z)+","+str(p)+'\n')
#            file_out.write("("+str(x)+", "+str(y)+", "+ str(z)+")"+'\n')
#            bpy.ops.mesh.primitive_cube_add(radius=p, location=(x,y,z))

file_out.close
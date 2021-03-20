from pycat.window import Window

window = Window()
msg= input("which animal do you want to see?")

animal=window.create_sprite()

if msg=="pig":
    animal.image="pig.png"
if msg=="rat":
    animal.image="rat.png"
if msg=="tiger":
    animal.image="tiger.png"
if msg=="owl":
    animal.image="owl.png"

size= input("how about the size? ")
animal.scale=float(size)


x= input("how about the x?")
animal.x=float(x)


y= input("how about the y?")
animal.y=float(y)

a=input("how about the rotation")
animal.rotation=float(a)

print(animal.x,",",animal.y,animal.image,animal.scale,animal.rotation)

window.run()
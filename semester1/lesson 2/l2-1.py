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

size= input("big or small? ")
if size=="big":
    animal.scale=2
if size=="small":
    animal.scale=0.5



where= input("left or right? ")
if where=="left":
    animal.x=20
    
if where=="right":
    animal.x=1000
    animal.y=300


where= input("top or bottom?")
if where=="top":
    animal.y=700

if where=="bottom":
    animal.y=50

print("position",animal.x,",",animal.y,animal.image,animal.scale)




window.run()
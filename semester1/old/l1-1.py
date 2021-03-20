from pycat.window import Window

window = Window()
msg= input("which animal do you want to see")

animal=window.create_sprite()

if msg=="pig":
    animal.image="pig.png"

if msg=="rat":
    animal.image="rat.png"

if msg=="tiger":
    animal.image="tiger.png"

if msg=="owl":
    animal.image="owl.png"
# if animal=="pig":
#     pig=window.create_sprite()
#     pig.image="pig.png"
#     pig.x=300
#     pig.y=400

# if animal=="rat":
#     rat=window.create_sprite()
#     rat.image="rat.png"
#     rat.x=500
#     rat.y=400

# if animal=="tiger":
#     tiger=window.create_sprite()
#     tiger.image="tiger.png"
#     tiger.x=700
#     tiger.y=400
    
# if animal=="owl":
#     owl=window.create_sprite()
#     owl.image="owl.png"
#     owl.x=900
#     owl.y=400

size= input("how big? ")
if size=="big":
    animal.scale=2
if size=="small":
    animal.scale=0.5



where= input("left or right ")
if where=="left":
    animal.x=20
    
if where=="right":
    animal.x=100
    animal.y=300


where= input("top or bottom")
if where=="top":
    animal.y=300


window.run()
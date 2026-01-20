import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 140
x2 = -250
y2 = 50
x3 = -250
y3 = -75
x4 = -250
y4 = -220


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("track")
basketball = create_sprite("basketball",x1,y1)
alien = create_sprite("alien",x2,y2)
cardinal = create_sprite("cardinal",x3,y3)
fish = create_sprite("fish",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # fastest is cardinal with average speed 13 then basketball with average speed 12.5, then alien with average speed 10.5 then fish with average speed 10
for i in range(30):
    x1 += random.randint (10,15)
    x2 += random.randint (5,16)
    x3 += random.randint (5,21)
    x4 += random.randint (0,20)

    basketball.goto(x1, y1)
    alien.goto(x2, y2)
    cardinal.goto(x3, y3)
    fish.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("basketball wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("alien wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("cardinal wins!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
    print("fish wins!")

turtle.exitonclick()
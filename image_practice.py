# Section 1 - Your code
from utils import *
set_background("moon")

s1 = create_sprite("balloon", 20, 100)
s2 = create_sprite("balloon", -60, -90)
s2 = create_sprite("rock_climbers", 50, -100)

message1 = create_sprite("alien",-260,200)
message1.color("red")
message1.write("Leo",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-260,100)
message2.color("red")
message2.write("cool picture",font = ("Arial", 40, "normal"))



######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
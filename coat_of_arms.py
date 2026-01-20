# Section 1 - Your code
from utils import *
set_background("brickwall")

s1 = create_sprite("coatarms", -20, 0)
s2 = create_sprite("cardinal", -100, 100)
s3 = create_sprite("cardinal", -100, -100)
s4 = create_sprite("lion", 0, 0)

message1 = create_sprite("alien",-200,200)
message1.color("black")
message1.write("Leo",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()
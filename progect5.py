import turtle, math, time, random
from utils import *

#in my game, mcdonalds and burger king fight over the moon by shooting french fries at  each other

#section 1: setup
set_background("moon")
smcd = create_sprite("mcfries",-300,0)
sbk = create_sprite("bkfries",300,0)

message_sprite = create_sprite("alien", -340,220)
message_sprite.hideturtle()

message_sprite1 = create_sprite("alien", 100,220)
message_sprite1.hideturtle()

bk_health = 500
mcd_health = 500
sprite_list = []
sprite_list1 = []

# Section 2: Controls

def move_up1():
    x = smcd.xcor()
    y = smcd.ycor() + 20
    smcd.goto(x,y)

def move_down1():
    x = smcd.xcor()
    y = smcd.ycor() - 20
    smcd.goto(x,y)

window.onkeypress(move_down1, "s")
window.onkeypress(move_up1, "w")

def move_up2():
    x = sbk.xcor()
    y = sbk.ycor() + 20
    sbk.goto(x,y)
        
def move_down2():
    x = sbk.xcor()
    y = sbk.ycor() - 20
    sbk.goto(x,y)

window.onkeypress(move_down2, "Down")
window.onkeypress(move_up2, "Up")

def bk_make_fry():
    bkfry = create_sprite("onefry", 300, sbk.ycor())
    sprite_list.append(bkfry)

def mcd_make_fry():
    mcdfry = create_sprite("onefry", -300,smcd.ycor())
    sprite_list1.append(mcdfry)

window.onkeypress(bk_make_fry, "Left")
window.onkeypress(mcd_make_fry, "d")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    for bkfry in sprite_list:
        x = bkfry.xcor() -5
        y = bkfry.ycor() 
        bkfry.goto(x,y)
        if get_distance(bkfry, smcd) < 100:
            mcd_health -= 1

    for mcdfry in sprite_list1:
        x = mcdfry.xcor() +5
        y = mcdfry.ycor() 
        mcdfry.goto(x,y)
        if get_distance(mcdfry, sbk) < 100:
            bk_health -= 1

    message_sprite.clear()
    message_sprite.write(f"Health: {mcd_health}",font = ("Arial", 30, "normal"))

    message_sprite1.clear()
    message_sprite1.write(f"Health: {bk_health}",font = ("Arial", 30, "normal"))

    if mcd_health < 1:
        break

    if bk_health < 1:
        break

    time.sleep(0.01)
    window.update()
    
if mcd_health > bk_health:
    print("Mc Donalds has taken over the moon")
else:
    print("Burger King has taken over the moon")
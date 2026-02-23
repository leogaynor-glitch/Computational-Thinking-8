import time, turtle, random
from utils import *
# Section 1: Setup
set_background("brickwall")
s1 = create_sprite("cup",-50,0)
s2 = create_sprite("cup",80,0)
s3 = create_sprite("cup", -180,0)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

def show_ball():
    set_image(s1, "cup_showing_ball")
def hide_ball():
    set_image(s1, "cup")

window.onkeypress(show_ball, "1")
window.onkeyrelease(hide_ball, "1")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


def move_up2():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down2():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left2():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right2(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)


window.onkeypress(move_up2, "Up")
window.onkeypress(move_down2, "Down")
window.onkeypress(move_left2, "Left")
window.onkeypress(move_right2, "Right")

# Section 3: define other controls
def hide2():
    s2.hideturtle()
def show2():
    s2.showturtle()

window.onkeypress(hide2, "l")
window.onkeyrelease(show2, "l")


def move_up3():
    x = s3.xcor()
    y = s3.ycor() + 10
    s3.goto(x,y)
        
def move_down3():
    x = s3.xcor()
    y = s3.ycor() - 10
    s3.goto(x,y)
    
def move_left3():
    x = s3.xcor() - 10
    y = s3.ycor() 
    s3.goto(x,y)
    
def move_right3(): 
    x = s3.xcor() + 10
    y = s3.ycor() 
    s3.goto(x,y)


window.onkeypress(move_up3, "t")
window.onkeypress(move_down3, "g")
window.onkeypress(move_left3, "f")
window.onkeypress(move_right3, "h")

# Section 3: define other controls
def hide3():
    s3.hideturtle()
def show3():
    s3.showturtle()

window.onkeypress(hide3, "l")
window.onkeyrelease(show3, "l")





# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()
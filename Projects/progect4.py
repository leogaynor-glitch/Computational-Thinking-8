import turtle, time, random
from utils import *

# Section 1 - setup
# in my game you get cheese and bread, then make grilled cheeses with them, which you spend on pans to make more grilled cheeses at the same time and try not to die
# TODO - set a background using set_background()
set_background("gc")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
cheese = 0
bread = 0
grilled_cheese = 0
pans = 1
hungry = 100
time_score = 0
time_scaling = 1

# these display my variables 
message_sprite = create_sprite("alien", -340,220)
message_sprite.hideturtle()

message_sprite1 = create_sprite("lion", -340,170)
message_sprite1.hideturtle()

message_sprite2 = create_sprite("bike", -340,120)
message_sprite2.hideturtle()

message_sprite3 = create_sprite("fish", -340,70)
message_sprite3.hideturtle()

message_sprite4 = create_sprite("balloon", -340,20)
message_sprite4.hideturtle()

message_sprite5 = create_sprite("can", -340,-30)
message_sprite5.hideturtle()

# Section 2 - controls
# these are the buttons you can use. they do cool stuff
#c gets you one times the amount of pans cheese
def get_cheese():
    global cheese
    cheese += pans
    x = random.randint (-400,400)
    y = random.randint (-400,400)
    create_sprite("cheese",x,y)
window.onkeypress(get_cheese, "c")

#b gets you one times the amount of pans bread
def get_bread():
    global bread
    bread += pans
    x = random.randint (-400,400)
    y = random.randint (-400,400)
    create_sprite("bread",x,y)
window.onkeypress(get_bread, "b")
# TODO - make a second control

#g gets you one times the amount of pans grilled cheeses if you have 2 times pans bread and one time pans cheese
def get_gc():
    global grilled_cheese, cheese, bread
    if cheese >= pans and bread >= 2*pans:
        grilled_cheese += pans
        cheese -= pans
        bread -= 2*pans
        x = random.randint (-400,400)
        y = random.randint (-400,400)
        create_sprite("grill_cheese",x,y)
window.onkeypress(get_gc, "g")

# p spends 3 grilled cheeses to get a pan, which helps you scale to keep up with hunger scaling
def acquire_pan():
    global pans, grilled_cheese
    if grilled_cheese >= 3:
        pans += 1
        grilled_cheese -= 3
        x = random.randint (-400,400)
        Y = random.randint (-400,400)
        create_sprite("pan",x,Y)
window.onkeypress(acquire_pan, "p")

# e eats one grilled cheese for 2 hunger to keep you alive
def eat_gc():
    global hungry, grilled_cheese
    if grilled_cheese >= 1:
        hungry += 2
        grilled_cheese -= 1
window.onkeypress(eat_gc, "e")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    if i % 100 == 0:
        time_scaling += .5
        hungry -= time_scaling
        time_score += 1
    # OPTIONAL - use the message sprite to say a message
# these three end the game when you starve and tell you 
    if hungry <= 0:
        print(f"you survived {time_score} time with {grilled_cheese} grilled cheeses.")
        quit()

    message_sprite1.clear()
    message_sprite1.write(f"Bread: {bread}",font = ("Arial", 30, "normal"))

    message_sprite.clear()
    message_sprite.write(f"Cheese: {cheese}",font = ("Arial", 30, "normal"))

    message_sprite2.clear()
    message_sprite2.write(f"Grilled Cheeses: {grilled_cheese}",font = ("Arial", 30, "normal"))

    message_sprite3.clear()
    message_sprite3.write(f"Pans: {pans}",font = ("Arial", 30, "normal"))

    message_sprite4.clear()
    message_sprite4.write(f"Hunger: {hungry}",font = ("Arial", 30, "normal"))

    message_sprite5.clear()
    message_sprite5.write(f"time: {time_score}",font = ("Arial", 30, "normal"))


    time.sleep(0.01)
    window.update()
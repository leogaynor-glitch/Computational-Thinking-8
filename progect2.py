basketball = 0
lacrosse = 0
soccer = 0
baseball = 0
input("welcome to my sports quiz.")
input("this quiz will tell you what sport you should try")
input("please answer with capital letters")

answer1 = input("do you like A) contact B) medium or low contact or C) no contact ")
if answer1 == "A": 
     lacrosse += 1
elif answer1 == "B": 
     soccer += 1
     basketball += 1 
elif answer1 == "C": 
     baseball += 1
elif answer1 == "a" or answer1 == "b" or answer1 == "c":
     print("I told you to use UPPERCASE LETTERS, you dont get to play sports")
     quit()

answer2 = input("would you prefer participating in a game where you are in A) nonstop action B) rare action or C) almost no action ")
if answer2 == "A": 
     basketball += 1
     lacrosse += 1
elif answer2 == "B": 
     soccer += 1
elif answer2 == "C": 
     baseball += 1

answer3 = input("do you prefer A) goals B) hoops or C) a square thing on the ground ")
if answer3 == "A": 
     soccer += 1
     lacrosse += 1
elif answer3 == "B": 
     basketball += 1
elif answer3 == "C": 
     baseball += 1


answer4 = input("do you like, A) super high score B) medium score or C) Low score ")
if answer4 == "A": 
     basketball += 1
elif answer4 == "B": 
     baseball += 1
     lacrosse += 1
elif answer4 == "C": 
     soccer+= 1

answer5 = input("would you play on A) grass B) floor or C) dirt and grass ")
if answer5 == "A": 
     lacrosse += 1
     soccer += 1
elif answer5 == "B": 
     basketball += 1
elif answer5 == "C": 
     baseball+= 1


if lacrosse > soccer and lacrosse > baseball and lacrosse > basketball:
     print("you should play lacrosse")
elif lacrosse < soccer and soccer > baseball and soccer > basketball:
     print("you should play soccer")
elif baseball > soccer and lacrosse < baseball and baseball > basketball:
     print("you should play baseball")
elif basketball > soccer and basketball > baseball and lacrosse < basketball:
     print("you should play basketball")
elif 0 == soccer == baseball == basketball == lacrosse:
     print("I guess you dont like sports")
print(f"soccer {soccer}")
print(f"lacrosse {lacrosse}")
print(f"baseball {baseball}")
print(f"basketball {basketball}")
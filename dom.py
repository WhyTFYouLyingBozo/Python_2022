from adventurelib import *
@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with the gold hairbrush that you have selected from the red basket 
		""")
	space = Room("""
	You are drifting in space. It feels very cold. A slate-blue spaceship sits completely silently to your left,it's airlock open and waiting 
	""" )
	spaceship = Room("""
		The bridge if the spaceship is shiny and white, with thousands of small, red, blinking lights.
		""")
current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
def enter_spaceship():
	global currrent_room
#check if action can be done
if current_room is not space:
	say("there is no airlock here")
	return
def main():
	start()

if __name__ == '__main__':
	main()
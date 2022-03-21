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
	quarters = Room("""
		This is the quarters, most of the contolling and organising is done here 
		""")
	mass_hall = Room("""
		This is the mass hall, mostly where everyone is and a great place to chill
		""")
	hallway = Room("""
		This is the hallway. It connects most of the rooms together
		""")
	cargo = Room("""
		This is Cargo, this is where most of the luggage,food and other things are kept
		""")
	docking = Room("""
		This is Docking, where we recieve and have stuff arrive
		""")
	bridge = Room("""
		This is the bridge, it connects the hallway to the escape pods.
		""")
	escape_pods = Room("""
		These are the escape pods, in emergencies, these are very crucial.
		""")
	current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global currrent_room
#check if action can be done
	if current_room is not space:
		say("there is no airlock here")
		return
	else:
		current_room = enter_spaceship
		print("""You leave yourself into the spaceship and slam your hand on the button to close the door.
			""")
		print(current_room)
def main():
	start()

if __name__ == '__main__':
	main()
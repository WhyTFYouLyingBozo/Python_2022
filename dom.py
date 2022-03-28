from adventurelib import *
Room.items = Bag()
space = Room("""
You are drifting in space. It feels very cold. A slate-blue spaceship sits completely silently to your left,it's airlock open and waiting 
""" )
spaceship = Room("""
	The bridge if the spaceship is shiny and white, with thousands of small, red, blinking lights.
	""")
quarters = Room("""
	This is the quarters, most of the contolling and organising is done here 
	""")
goggles.items.add(goggles)
mass_hall = Room("""
	This is the mass hall, mostly where everyone is and a great place to chill
	""")
	mass_hall.items.add(red_keycard)
hallway = Room("""
	This is the hallway. It connects most of the rooms together
	""")
cargo = Room("""
	This is Cargo, this is where most of the luggage,food and other things are kept
	""")
cargo.items.add(knife)
docking = Room("""
	This is Docking, where we recieve and have stuff arrive
	""")
bridge = Room("""
	This is the bridge, it connects the hallway to the escape pods.
	""")
USB.items.add(USB)
escape_pods = Room("""
	These are the escape pods, in emergencies, these are very crucial.
	""")
current_room = space
	
spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mass_hall
quarters.east = mass_hall
cargo.east = docking
bridge.south = escape_pods

@when ("go DIRECTION")
def travel(direction):
	global currrent_room
	if direction in current_room.exits():
		currrent_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)

@when("Look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out each item

Item.description - "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard", "red card",)
red_keycard.description = "It's a red keycard. It probably opens a door or a locker."

goggles = Item("goggles", "glasses")
goggles.description = "Round circular goggles, help to see certain things the naked eye can't"

USB = Item("USB", "usb", "Usb")
USB.description = "Regular USB, but it stores some interesting files..."

#define variables
current_room = space
inventory = bag()

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock
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
	print(current_room)
	start()

if __name__ == '__main__':
	main()
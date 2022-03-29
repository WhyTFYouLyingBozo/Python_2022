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
	
spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mass_hall
quarters.east = mass_hall
cargo.east = docking
bridge.south = escape_pods


Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard", "red card")
red_keycard.description = "It's a red keycard. It probably opens a door or a locker."

goggles = Item("goggles", "glasses")
goggles.description = "Round circular goggles, help to see certain things the naked eye can't"

usb = Item("USB", "usb", "Usb")
usb.description = "Regular USB, but it stores some interesting files..."

mass_hall.items.add(red_keycard)
quarters.items.add(usb)
hallway.items.add(goggles)
cargo.items.add(knife)

#define variables
current_room = space
inventory = Bag()


@when ("go DIRECTION")
def travel(direction):
	global currrent_room
	if direction in current_room.exits():
		currrent_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)

@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out each item

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a dull{items}")	

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")


@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check if action can be done
	if current_room is not space:
		say("there is no airlock here")
		return
	else:
		current_room = spaceship
		print("You leave yourself into the spaceship and slam your hand on the button to close the door.")
		print(current_room)


def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()
from adventurelib import *
Room.items = Bag()
inventory = Bag()


#rooms of game
kings_tomb = Room(""" This is King Hotemprah's room, filled with treasures no eye has ever seen,\n
 gold as bright as the sun. Don't be greedy.
	""")
queens_tomb = Room(""" This is the Queens room, you will find treasures as well but have a look around, there might just be something interesting.
	""")
scepter_room = Room(""" The room of the scepter, taken straight from Indiana Jones,this also shows a map of the pyramid,however the naked eye can't see, not without a little red however.

	""")
hallway = Room("""
This is the hallway, it connects the rooms together, look out for some hidden extras.
	""")
snake_room = Room(""" You enter, Snakes hiss loudly, what can you do to silence them? They are what stands between you and Ra's orb which can be used to unlock a certain door. 
	""")
puzzle_room = Room (""" Solve the ancient puzzle by inserting the right key to release the heart of anubis, which might come in handy.
	""")
the_wall = Room(""" congrats, you have conquered all tasks, place each items in their places
 and enter the secret code to escape.""")

outside_pyramid = Room(""" You did it, you made it through, now you may go present the treasures of the great Pharaoh King Hotemprah.
	""")

#connections for rooms
kings_tomb.west = queens_tomb
queens_tomb.south = hallway
hallway.west = scepter_room
hallway.south = snake_room
snake_room.west = puzzle_room
puzzle_room.south = the_wall
the_wall.east = outside_pyramid 

#items
Item.description = ""

hotemprahs_skin = Item("hotemprahs skin", "skin")
hotemprahs_skin.description = "This is the grand treasue of hotemprah, because he was dumb this mask is designed to translate hieroglyphics into english, use it well."

lenses = Item("glasses", "lenses")
lenses.desctiption = "These lenses look regular at first but they help you to see beyond the eye"

the_code = Item("code")
the_code.description = "This code unlocks, something, this isn't one you keep so remember. 49658"

key1 = Item("key1", "1")
key1.description = "This key might be ordinary, but will be useful, or not. pick right"

key2 = Item("key2")
key2.desctiption = "This key might be ordinary, but will be useful, or not. pick right"

flute = Item("flute", "whistle")
flute.description = "The flute might look ordinary, can silence a crowd however"

limestone_knife = Item("knife", "limestone knife")
limestone_knife.description = "Limestone was a powerful rock used to build houses and what not, now in knife form, useful, no?"

anubis_heart = Item("gem", "anubis heart")
anubis_heart.description = "The green and most purest gem, you have earnt it. Hold onto it and give it your heart."

#placing items in rooms
kings_tomb.items.add(hotemprahs_skin) 
kings_tomb.items.add(lenses)
queens_tomb.items.add(limestone_knife)
queens_tomb.items.add(flute)
hallway.items.add(the_code)
scepter_room.items.add(key1)
scepter_room.items.add(key2)
puzzle_room.items.add(anubis_heart)

current_room = kings_tomb
inventor = Bag()
#take item code
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")

#direction code so players can move
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("You can't go that way")

#look for items to use and take
@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room
		print("You also see:")
		for item in current_room.items:
			print(item)#print out each item
	
#what items you have
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("use ITEM")
def use(item):
	if inventory.find(item) ==


def main():
	print(current_room)
	start()

if __name__ == '__main__':
	main()

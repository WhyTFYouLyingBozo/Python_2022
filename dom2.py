from adventurelib import *
#Room.items = Bag()


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
snake_room = Room(""" You enter, Snakes hiss loudly, what can you do to silence them? They are what stands between you and Cleopatra's 'heart' which can be used to unlock a certain door. 
	""")
puzzle_room = Room (""" Solve the ancient puzzle by inserting the right key to release the stone of bezel, which might come in handy.
	""")
the_wall = Room(""" congrats, you have conquered all tasks, place each items in their places
 and enter the secret code to escape.""")

outside_pyramid = Room(""" You did it, you made it through, now you may go present the treasures of the great Pharaoh King Hotemprah.
	""")

#connections for rooms
current_room = kings_tomb
kings_tomb.south = queens_room
queens_room.south = hallway
hallway.west = scepter_room
hallway.south = snake_room
snake_room.south = puzzle_room
puzzle_room.east = the_wall
the_wall.north = outside_pyramid 

#items
Item.description = ""

hotemprahs_skin = Item("hotemprahs skin", "skin")
hotemprahs_skin.description = "This is the grand treasue of hotemprah, because he was dumb this mask is designed to translate hieroglyphics into english, use it well."

lenses = Item("glasses", "lenses")
lenses.desctiption = "These belonged to the great Cleopatra, regular at first but they help you to see beyond the eye"

charm_of_bezel = Item("charm","charm of bezel", "bezel")
charm_of_bezel.description = "Another one of Cleopatra's assets, can project a view and layout in the map room ogf the map"

the_code = Item("code")
the_code.description = "This code unlocks, something, this isn't one you keep so remember. 49658"



def main():
	#print(current_room)
	start()

if __name__ == '__main__':
	main()

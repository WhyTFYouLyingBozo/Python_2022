from adventurelib import *
#Room.items = Bag()

print(f"You have secured the treasure of King Hotemprah.\n Now  you must make your way through the pyramid through the Thick and thin and reach the bottom,\n one wrong however and you could be stuck for an eternity.\n Good Luck!, you will need it." )

kings_tomb = Room(""" This is King Hotemprah's room, filled with treasures no eye has ever seen,\n
 gold as bright as the sun. Don't be greedy.
	""")
queens_room = Room(""" This is the Queens room, you will find treasures as well but have a look around, there might just be something interesting.
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

current_room = kings_tomb
kings_tomb.east = queens_room
kings_tomb.south = hallway
queens_room.south = hallway


def main():
	#print(current_room)
	start()

if __name__ == '__main__':
	main()

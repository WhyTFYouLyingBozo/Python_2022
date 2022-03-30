from adventurelib import *
#Room.items = Bag()

print(f"You have secured the treasure of King Hotemprah.\n Now  you must make your way through the pyramid through the Thick and thin and reach the bottom,\n one wrong however and you could be stuck for an eternity.\n Good Luck!, you will need it." )

kings_tomb = Room(""" This is King Hotemprah's room, filled with treasures no eye has ever seen,\n
 gold as bright as the sun. Don't be greedy.
	""")
queens_room = Room(""" This is the Queens room,\n
	you will find treasures as well but have a look around, there might just be something interesting.


	""")


def main():
	#print(current_room)
	start()

if __name__ == '__main__':
	main()

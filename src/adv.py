from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

player = Player("One", "foyer")
playing = True
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
print("Current Room:", player.current_room)

while playing:
    # * Waits for user input and decides what to do.
    user_input = input(
        "Where do you want to go? North [n], East [e], South [s], West [w]? Or 'q' to quit: ")
    select = False

    if user_input == 'n':
        try:
            select = True
            player.current_room = room[player.current_room].n_to.name
        except:
            print("Can't Go There!")

    elif user_input == 'e':
        try:
            select = True
            player.current_room = room[player.current_room].e_to.name
        except:
            print("Can't Go There!")

    elif user_input == 's':
        try:
            select = True
            player.current_room = room[player.current_room].s_to.name
        except:
            print("Can't Go There!")

    elif user_input == 'w':
        try:
            select = True
            player.current_room = room[player.current_room].w_to.name
        except:
            print("Can't Go There!")

# If the user enters "q", quit the game.
    elif user_input == 'q':
        print("Bye for now...")
        playing = False
    else:
        print("Try again, only with n, e, s, w... \n")

    if select == True:
        if player.current_room == 'Outside Cave Entrance':
            player.current_room = 'outside'
        elif player.current_room == 'Foyer':
            player.current_room = 'foyer'
        elif player.current_room == 'Grand Overlook':
            player.current_room = 'overlook'
        elif player.current_room == 'Narrow Passage':
            player.current_room = 'narrow'
        elif player.current_room == 'Treasure Chamber':
            player.current_room = 'treasure'

        player.current_room = player.current_room.lower()

        description = room[player.current_room].description
        print(
            f"\n You are currently located {player.current_room}, \n {description} \n")
        select = False

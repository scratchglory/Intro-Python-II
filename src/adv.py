from room import Room
from player import Player

# Declare all the rooms

# room = {
#     'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

#     'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

#     'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
# }

outside = Room("Outside Cave Entrance",
               "North of you, the cave mount beckons"),

foyer = Room(
    "Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

narrow = Room("Narrow Passage",
              """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

treasure = Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),


# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

outside[0].n_to = foyer[0].name
foyer[0].s_to = outside[0].name
foyer[0].n_to = overlook[0].name
foyer[0].e_to = narrow[0].name
overlook[0].s_to = foyer[0].name
narrow[0].w_to = foyer[0].name
narrow[0].n_to = treasure[0].name
treasure[0].s_to = narrow[0].name

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

player = Player("One", outside)
playing = True
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
cr = player.current_room
print("Current Room:", cr[0].name)

while playing:
    # * Waits for user input and decides what to do.
    user_input = input(
        "Where do you want to go? North [n], East [e], South [s], West [w]? Or 'q' to quit: ")
    select = False

    if user_input == 'n':
        try:
            select = True
            cr = cr[0].n_to
        except:
            print("Can't Go There!")

    elif user_input == 'e':
        try:
            select = True
            cr = cr[0].e_to
        except:
            print("Can't Go There!")

    elif user_input == 's':
        try:
            select = True
            cr = cr[0].s_to
        except:
            print("Can't Go There!")

    elif user_input == 'w':
        try:
            select = True
            cr = cr[0].w_to
        except:
            print("Can't Go There!")

# If the user enters "q", quit the game.
    elif user_input == 'q':
        print("Bye for now...")
        playing = False
    else:
        print("Try again, only with n, e, s, w... \n")

    if select == True:
        if cr == 'Outside Cave Entrance':
            cr = outside
        elif cr == 'Foyer':
            cr = foyer
        elif cr == 'Grand Overlook':
            cr = overlook
        elif cr == 'Narrow Passage':
            cr = narrow
        elif cr == 'Treasure Chamber':
            cr = treasure

        print(
            f"""You are currently located {cr[0].name}. \n Description: {cr[0].description} \n""")
        select = False

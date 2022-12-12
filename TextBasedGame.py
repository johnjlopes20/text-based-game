# JOHN LOPES
# IT 140 Project 2
# TEXT BASED GAME


# Print instructions
print("You've landed in Verdansk")
print("Collect all 6 items and defeat the Juggernaut before he takes over")
print("Commands to move between rooms: go South, go North, go East, go West")
print("Command to pick up items: 'take' + 'item name'")

# dictionary with directions from each room and items in each room
locations = {'Downtown': {'name': 'Downtown', 'South': 'Tv Station', 'West': 'Promenade', 'North': 'Superstore', 'East': 'Quarry'},
         'Tv Station': {'name': 'Tv Station', 'East': 'Airport', 'North': 'Downtown', 'item': 'Self Revive'},
         'Airport': {'name': 'Airport', 'West': 'Tv Station', 'item': 'Ammunition'},
         'Promenade': {'name': 'Promenade', 'East': 'Downtown', 'item': 'Shields'},
         'Quarry': {'name': 'Quarry', 'West': 'Downtown', 'North': 'Port', 'item': 'Uav'},
         'Port': {'name': 'Port', 'South': 'Quarry'},
         'Superstore': {'name': 'Superstore', 'South': 'Downtown', 'East': 'Train Station', 'item': 'Pistol'},
         'Train Station': {'name': 'Train Station', 'West': 'Superstore', 'item': 'Grenades'},
    }
#movement between loactions
def movement(current_location, move, locations):
    current_location = locations[current_location][move]
    return current_location

# add item to items list
def take_items(current_location, move, locations, item):
    item.append(locations[current_location]['item'])
    del locations[current_location]['item']

# current room
current_location = "Downtown"
# list for items
items = []

# when player meets juggernaut
while True:
    if current_location == 'Port':
        if len(items) == 6:
            print('Congratulations you have defeated the Juggernaut and saved Verdansk!')
            print('Thanks for playing!')
            break
        else:
            print('The Juggernaut destroyed Verdansk!')
            print('You did not collect all of the items before fighting the Juggernaut!')
            print('Thanks for playing! Try Again!')
            break
    # display current room and items
    print('You are in the ' + current_location)
    print(items)
    # display item in the room
    if current_location != 'Port' and 'item' in locations[current_location].keys():
        print('There is a {}'.format(location[current_location]['item']))
    print()
    move = input('Where do you want to go: ').title().split()

    # move to a new room
    if len(move) >= 2 and move[1] in locations[current_location].keys():
        current_location = movement(current_location, move[1], locations)
        continue
    # pick up item
    elif len(move[0]) == 4 and move[0] == 'Take' and ' '.join(move[1:]) in locations[current_location]['item']:
        print('You picked up the {}'.format(locations[current_location]['item']))
        print()
        take_items(current_location, move, locations, items)
        continue
    # invalid command
    else:
        print('Invalid move, please try again')
        continue

rooms = {
    'Hall': {
        'description': 'You are in a grand hall. There is a table in the middle.',
        'north': 'Bedroom',
        'south': 'Kitchen',
        'item': None
    },
    'Bedroom': {
        'description': 'You are in a cozy bedroom. There is a bed and a wardrobe.',
        'south': 'Hall',
        'item': 'Key'
    },
    'Kitchen': {
        'description': 'You are in a kitchen. There is a strange smell in the air.',
        'north': 'Hall',
        'west': 'Garden',
        'item': 'Knife'
    },
    'Garden': {
        'description': 'You are in a beautiful garden. There are flowers blooming.',
        'east': 'Kitchen',
        'item': 'Shovel'
    }
}

inventory = []
current_room = 'Hall'

def describe_room(room):
    print(f"\n{rooms[room]['description']}")
    if rooms[room]['item']:
        print(f"You see a {rooms[room]['item']} here.")

def player_move(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        describe_room(current_room)
    else:
        print("You can't go that way!")

def pick_up_item():
    item = rooms[current_room]['item']
    if item:
        inventory.append(item)
        rooms[current_room]['item'] = None
        print(f"You picked up the {item}!")
    else:
        print("There's nothing to pick up here.")

def check_inventory():
    if inventory:
        print("You are carrying:", ", ".join(inventory))
    else:
        print("Your inventory is empty.")

def game():
    print("Welcome to the Text Adventure Game!")
    describe_room(current_room)
    
    while True:
        command = input("\nEnter a command (go [direction], pick up, inventory, quit): ").lower().split()

        if command[0] == "go":
            if len(command) == 2:
                player_move(command[1])
            else:
                print("Invalid move command. Use 'go [direction]'.")

        elif command[0] == "pick" and len(command) > 1 and command[1] == "up":
            pick_up_item()

        elif command[0] == "inventory":
            check_inventory()

        elif command[0] == "quit":
            print("Thank you for playing!")
            break

        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    game()

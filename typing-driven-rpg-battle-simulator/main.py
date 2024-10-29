import random
import json
import os

class Character:
    def __init__(self, name, health, magic):
        self.name = name
        self.health = health
        self.magic = magic

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.health += 10
        self.magic += 5
        print(f"{self.name} leveled up! Health: {self.health}, Magic: {self.magic}")

class Player(Character):
    def __init__(self, name, health=100, magic=100):
        super().__init__(name, health, magic)
        self.experience = 0
        self.level = 1
        self.inventory = {'health_potion': 2}
        self.special_attack_used = False

    def attack(self, enemy, spell):
        if spell in spells:
            damage = spells[spell]['damage']
            cost = spells[spell]['cost']
            if self.magic >= cost:
                self.magic -= cost
                enemy.health -= damage
                print(f"{self.name} casts {spell} and deals {damage} damage!")
            else:
                print(f"Not enough magic to cast {spell}!")
        else:
            print("Invalid spell name! Try again.")

    def use_health_potion(self):
        if self.inventory['health_potion'] > 0:
            self.health += 20
            self.inventory['health_potion'] -= 1
            print(f"{self.name} used a health potion! Health: {self.health}")
        else:
            print("No health potions left!")

    def special_attack(self, enemy):
        if not self.special_attack_used:
            damage = 50
            enemy.health -= damage
            self.special_attack_used = True
            print(f"{self.name} performs a special attack and deals {damage} damage!")
        else:
            print("Special attack can only be used once per battle!")

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience!")
        if self.experience >= 100:  # Level up condition
            self.experience = 0
            self.level_up()

class Enemy(Character):
    def __init__(self, name, health=50):
        super().__init__(name, health)

def show_status(player, enemies):
    print(f"\n{player.name} - Health: {player.health}, Magic: {player.magic}, Level: {player.level}, Potions: {player.inventory['health_potion']}")
    for enemy in enemies:
        print(f"{enemy.name} - Health: {enemy.health}")

def player_turn(player, enemies):
    while True:
        action = input("Choose action: (1) Spell (2) Health Potion (3) Special Attack: ").strip()
        
        if action == '1':
            spell = input("Type your spell: ").strip().lower()
            for enemy in enemies:
                if enemy.is_alive():
                    player.attack(enemy, spell)
                    if enemy.health <= 0:
                        print(f"{enemy.name} has been defeated!")
                        player.gain_experience(50)  # Gain XP for defeating an enemy
                    return

        elif action == '2':
            player.use_health_potion()
            return

        elif action == '3':
            for enemy in enemies:
                if enemy.is_alive():
                    player.special_attack(enemy)
                    if enemy.health <= 0:
                        print(f"{enemy.name} has been defeated!")
                        player.gain_experience(50)
                    return

        else:
            print("Invalid action! Try again.")

def enemy_turn(player, enemies):
    for enemy in enemies:
        if enemy.is_alive():
            damage = random.randint(5, 15)
            player.health -= damage
            print(f"{enemy.name} attacks {player.name} and deals {damage} damage!")

def battle(player, enemies):
    print(f"A wild {', '.join(enemy.name for enemy in enemies)} appear!")
    while player.is_alive() and any(enemy.is_alive() for enemy in enemies):
        show_status(player, enemies)
        player_turn(player, enemies)
        if not any(enemy.is_alive() for enemy in enemies):
            break
        enemy_turn(player, enemies)

    if player.is_alive():
        print("You emerged victorious!")
    else:
        print("You have been defeated!")

def save_game(player):
    with open("save_game.json", "w") as f:
        json.dump(player.__dict__, f)
    print("Game saved!")

def load_game():
    if os.path.exists("save_game.json"):
        with open("save_game.json", "r") as f:
            data = json.load(f)
            player = Player(data['name'], data['health'], data['magic'])
            player.experience = data['experience']
            player.level = data['level']
            player.inventory = data['inventory']
            player.special_attack_used = data['special_attack_used']
            print("Game loaded!")
            return player
    else:
        print("No save file found. Starting a new game.")
        return None

# Define spells with their damage and cost
spells = {
    'fireball': {'damage': 25, 'cost': 10},
    'ice shard': {'damage': 15, 'cost': 5},
    'lightning strike': {'damage': 30, 'cost': 20},
    'heal': {'damage': -20, 'cost': 15},  # Heal spell (negative damage)
}

if __name__ == "__main__":
    print("Welcome to the Typing-Driven RPG Battle Simulator!")
    choice = input("Do you want to (1) Start a new game or (2) Load a saved game? ")
    player = None

    if choice == '1':
        player_name = input("Enter your character's name: ")
        player = Player(player_name)
    elif choice == '2':
        player = load_game()
        if player is None:
            player_name = input("Enter your character's name: ")
            player = Player(player_name)

    enemies = [Enemy("Goblin"), Enemy("Orc"), Enemy("Troll")]
    battle(player, enemies)

    save_game(player)

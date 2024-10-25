# Typing-Driven RPG Battle Simulator

A text-based RPG battle game where players can cast spells, use items, and battle multiple enemies. The game features a save/load system, character progression, and various combat mechanics.

## Features

- **Character System**
  - Create a custom character with health and magic points
  - Level up system with experience gains
  - Character stats increase upon leveling up
  - Save and load game progress

- **Combat System**
  - Turn-based battles against multiple enemies
  - Various spells with different damage and magic costs
  - Special attack ability (once per battle)
  - Health potions for recovery
  - Dynamic battle status updates

- **Spells**
  - Fireball (25 damage, 10 MP)
  - Ice Shard (15 damage, 5 MP)
  - Lightning Strike (30 damage, 20 MP)
  - Heal (-20 damage, 15 MP)

## Getting Started

### Prerequisites
- Python 3.x
- No additional packages required

### Installation
1. Clone the repository or download the `main.py` file
2. Navigate to the game directory in your terminal
3. Run the game:
```bash
python main.py
```

## How to Play

1. **Starting the Game**
   - Choose between starting a new game or loading a saved game
   - For new games, enter your character's name

2. **Battle System**
   - Each turn, choose from three actions:
     1. Cast a spell
     2. Use a health potion
     3. Perform a special attack
   
   - After your action, enemies will automatically take their turns

3. **Spells and Combat**
   - Type the exact spell name when casting (e.g., "fireball", "ice shard")
   - Monitor your magic points (MP) - each spell has a cost
   - Use health potions strategically - you start with 2
   - Special attack deals high damage but can only be used once per battle

4. **Character Progress**
   - Gain experience by defeating enemies
   - Level up at 100 experience points
   - Each level up increases health by 10 and magic by 5

5. **Saving Progress**
   - The game automatically saves after each battle
   - Load your progress when starting the game

## Game Stats

### Player Starting Stats
- Health: 100
- Magic: 100
- Level: 1
- Experience: 0
- Health Potions: 2

### Enemy Stats
- Goblin: 50 HP
- Orc: 50 HP
- Troll: 50 HP

## Contributing

Feel free to fork the repository and submit pull requests with improvements. Some potential areas for enhancement:
- Additional spells and abilities
- More enemy types
- Equipment system
- Multiple battle scenarios
- Enhanced user interface

## License

This project is free to use and modify.
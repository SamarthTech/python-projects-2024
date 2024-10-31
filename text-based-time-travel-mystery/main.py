import time

class TimePeriod:
    def __init__(self, name, description, clues):
        self.name = name
        self.description = description
        self.clues = clues

    def get_clue(self):
        if self.clues:
            return self.clues.pop(0)
        return None

class Character:
    def __init__(self, name, dialogue, clues):
        self.name = name
        self.dialogue = dialogue
        self.clues = clues

    def talk(self):
        print(f"{self.name}: {self.dialogue}")

    def give_clue(self):
        if self.clues:
            return self.clues.pop(0)
        return None

class Game:
    def __init__(self):
        self.inventory = []
        self.time_periods = []
        self.current_period_index = 0
        self.characters = []
        
        # Define time periods
        self.setup_time_periods()
        # Define characters
        self.setup_characters()

    def setup_time_periods(self):
        ancient_egypt = TimePeriod(
            "Ancient Egypt",
            "You find yourself in ancient Egypt, surrounded by pyramids.",
            ["The Pharaoh's secret is buried deep.", "Look for the Sphinx's riddle."]
        )
        
        medieval_england = TimePeriod(
            "Medieval England",
            "You are in a bustling medieval town filled with knights.",
            ["The sword of destiny lies within the castle.", "A dragon guards the treasure."]
        )

        future_city = TimePeriod(
            "Future City",
            "You've traveled to a high-tech future where robots roam.",
            ["The key to the city is hidden in the AI core.", "The holographic map reveals the path."]
        )

        self.time_periods = [ancient_egypt, medieval_england, future_city]

    def setup_characters(self):
        sphinx = Character("Sphinx", "Solve my riddle to proceed!", ["What walks on four legs in the morning, two legs in the afternoon, and three legs in the evening?"])
        knight = Character("Knight", "I seek the brave who can retrieve the sword.", ["Only the worthy may claim it."])
        robot = Character("Robot", "Greetings, human. I have a task for you.", ["Find the core to unlock the city."])

        self.characters = [sphinx, knight, robot]

    def display_intro(self, time_period):
        print(f"\n--- Welcome to the {time_period.name} ---")
        print(time_period.description)
        time.sleep(2)

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"Added to inventory: {item}")

    def show_inventory(self):
        if self.inventory:
            print("\nYour Inventory:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("\nYour inventory is empty.")

    def play_game(self):
        while self.current_period_index < len(self.time_periods):
            current_period = self.time_periods[self.current_period_index]
            self.display_intro(current_period)

            # Show clue
            clue = current_period.get_clue()
            if clue:
                print(f"Clue: {clue}")
                self.add_to_inventory(clue)  # Add clues to inventory

            # Character interaction
            for character in self.characters:
                action = input(f"\nDo you want to talk to {character.name}? (yes/no): ")
                if action.lower() == "yes":
                    character.talk()
                    clue_from_character = character.give_clue()
                    if clue_from_character:
                        print(f"Clue from {character.name}: {clue_from_character}")
                        self.add_to_inventory(clue_from_character)

            # Show inventory after actions
            self.show_inventory()

            # Choose next time period or repeat
            action = input("\nDo you want to (1) continue to the next time period or (2) go back? ")
            if action == "1":
                self.current_period_index += 1
            elif action == "2":
                if self.current_period_index > 0:
                    self.current_period_index -= 1
                else:
                    print("You are already at the first time period.")
            else:
                print("Invalid input. Please choose 1 or 2.")

        print("\n--- You have completed your time-travel adventure! ---")

if __name__ == "__main__":
    game = Game()
    game.play_game()

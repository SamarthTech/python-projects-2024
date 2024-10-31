import time
import random

# Expanded list of regional teas and their typical ingredients
regional_teas = {
    "Indian Masala Chai": ["black tea", "ginger", "cardamom", "cinnamon", "cloves", "milk"],
    "Japanese Matcha": ["matcha", "water", "milk"],
    "Moroccan Mint Tea": ["green tea", "mint", "sugar"],
    "Taiwanese Bubble Tea": ["black tea", "green tea", "tapioca", "milk", "sugar"],
    "English Breakfast Tea": ["black tea", "milk", "sugar"],
    "South African Rooibos": ["rooibos", "honey", "lemon"],
    "Chinese Oolong Tea": ["oolong tea", "water", "jasmine", "ginger"],
    "Turkish Tea": ["black tea", "sugar", "lemon"],
    "Thai Iced Tea": ["black tea", "condensed milk", "spices", "sugar", "ice"],
    "Argentinian Yerba Mate": ["yerba mate", "water", "lemon", "mint"],
    "Russian Tea": ["black tea", "jam", "lemon"],
    "Egyptian Hibiscus Tea": ["hibiscus", "sugar", "lemon"],
    "Kenyan Purple Tea": ["purple tea", "honey", "ginger", "lemon"],
    "Chilean Patagonia Tea": ["herbal tea", "calafate berries", "mint", "honey"]
}

# Region associated with each tea
region_map = {
    "Indian Masala Chai": "India",
    "Japanese Matcha": "Japan",
    "Moroccan Mint Tea": "Morocco",
    "Taiwanese Bubble Tea": "Taiwan",
    "English Breakfast Tea": "England",
    "South African Rooibos": "South Africa",
    "Chinese Oolong Tea": "China",
    "Turkish Tea": "Turkey",
    "Thai Iced Tea": "Thailand",
    "Argentinian Yerba Mate": "Argentina",
    "Russian Tea": "Russia",
    "Egyptian Hibiscus Tea": "Egypt",
    "Kenyan Purple Tea": "Kenya",
    "Chilean Patagonia Tea": "Chile"
}

# Feedback messages for the tea evaluation
feedback = {
    "classic": "You made a comforting classic blend, perfect for relaxing afternoons!",
    "bold": "You created a bold, exotic tea bursting with new flavors!",
    "clash": "Oops! The flavors might be a bit overpowering. Try tweaking a few ingredients for a better taste!"
}

# Function to rate the tea based on complexity
def rate_tea(ingredients, time_taken):
    if len(ingredients) <= 3:
        return random.randint(1, 5)  # Simpler tea, lower score range
    elif len(ingredients) <= 6:
        return random.randint(5, 8)  # Medium complexity
    else:
        return random.randint(8, 10)  # High complexity, higher score

# Function to evaluate the tea based on ingredients and time taken
def evaluate_tea(ingredients, time_taken, tea_strength, sweetened):
    matched_teas = {}
    
    # Check how many ingredients match each regional tea
    for tea, region_ingredients in regional_teas.items():
        match_count = sum(1 for item in ingredients if item in region_ingredients)
        
        if match_count > 0:
            matched_teas[tea] = match_count

    # Determine the feedback based on time taken
    if time_taken < 20:
        time_feedback = "Quick Brew"
    elif time_taken < 40:
        time_feedback = "Balanced Brew"
    else:
        time_feedback = "Complex Brew"
    
    # Check if multiple regions are involved
    if len(matched_teas) == 1:
        tea_name = list(matched_teas.keys())[0]
        return f"You made a tea from the {region_map[tea_name]} region ({tea_name})! {feedback['classic']} (Time: {time_feedback}, Strength: {tea_strength}, Sweetened: {sweetened})"
    elif len(matched_teas) > 1:
        # Fusion of different regions
        regions_involved = [region_map[tea] for tea in matched_teas.keys()]
        regions_string = ", ".join(regions_involved)
        return f"Wow! You created a unique fusion tea with ingredients from {regions_string}! {feedback['bold']} (Time: {time_feedback}, Strength: {tea_strength}, Sweetened: {sweetened})"
    else:
        # If no matching tea is found
        if len(ingredients) > 5:
            return f"{feedback['clash']} (Time: {time_feedback}, Strength: {tea_strength}, Sweetened: {sweetened})"
        else:
            return f"{feedback['bold']} (Time: {time_feedback}, Strength: {tea_strength}, Sweetened: {sweetened})"

# Function to get user input and play the game
def play_tea_game():
    print("Welcome to the Tea-Making Game!")
    print("Choose ingredients for your tea. Type 'done' when you're finished.")
    
    ingredients = []
    start_time = time.time()
    
    while True:
        ingredient = input("Add an ingredient: ").strip().lower()
        if ingredient == "done":
            break
        ingredients.append(ingredient)
    
    end_time = time.time()
    time_taken = int(end_time - start_time)
    
    # Customization options
    tea_strength = input("Choose tea strength (Light, Medium, Strong): ").strip().capitalize()
    sweetened = input("Do you want your tea sweetened? (Yes/No): ").strip().capitalize()
    
    print("\nBrewing your tea...")
    time.sleep(2)
    
    # Evaluate the tea and generate feedback
    result = evaluate_tea(ingredients, time_taken, tea_strength, sweetened)
    print("\nResult:")
    print(result)
    
    # Rate the tea
    rating = rate_tea(ingredients, time_taken)
    print(f"Your tea blend gets a rating of {rating}/10!")
    
    # Option to name the tea
    tea_name = input("Would you like to name your tea? (Yes/No): ").strip().lower()
    if tea_name == "yes":
        custom_name = input("Enter a name for your tea: ").strip()
        print(f"\nGreat! Your tea blend is now called '{custom_name}'!")
    
    print("\nThanks for playing! Enjoy your tea!")

# Start the game
play_tea_game()

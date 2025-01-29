import config

def set_difficulty():
# Print / Select Difficulty
    while True:
        print("\n1. Easy\n2. Medium\n3. Hard")
        choice = input("\nPlease choose your level of Difficulty (1, 2, 3): ").strip()
        
        # Use string keys for matching
        difficulty = {
            "1": config.EASY,
            "2": config.MEDIUM,
            "3": config.HARD
        }.get(choice)
        
        if difficulty:
            # If valid choice, break the loop
            grid_size, num_words = difficulty  # Unpack the tuple (e.g., (10, 7))
            print(f"\nYou selected {choice}: Grid Size = {grid_size}, Number of Words = {num_words}")
            break
        else:
            # Invalid input, prompt again
            print("\nInvalid choice. Please select 1, 2, or 3.")
            
    return grid_size, num_words
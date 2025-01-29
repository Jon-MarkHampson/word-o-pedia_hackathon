import config

def set_difficulty():
    """ Set the difficulty level of the game """
    
    # Print / Select Difficulty
    print("Difficulty Levels:")
    while True:
        print(f"""
{config.Fore.GREEN} 1. Easy
{config.Fore.BLUE}  2. Medium
{config.Fore.LIGHTRED_EX}   3. Hard{config.Style.RESET_ALL}""")
        choice = input(f"\nPlease choose your level of Difficulty ({config.Fore.GREEN}1{config.Style.RESET_ALL} /{config.Fore.BLUE} 2 {config.Style.RESET_ALL}/ {config.Fore.LIGHTRED_EX}3{config.Style.RESET_ALL}): ").strip()
        
        # Use string keys for matching
        difficulty = {
            "1": config.EASY,
            "2": config.MEDIUM,
            "3": config.HARD
        }.get(choice)
        
        if difficulty:
            # If valid choice, break the loop
            # Unpack the tuple (e.g., (10, 7))
            grid_size, num_words, diff_string = difficulty  
            print(f"\nYou selected {config.COLOURS_LIST[int(choice)]}{diff_string}{config.Style.RESET_ALL}: Grid Size = {config.COLOURS_LIST[int(choice)]}{grid_size}{config.Style.RESET_ALL}, Number of Words = {config.COLOURS_LIST[int(choice)]}{num_words}{config.Style.RESET_ALL}")
            break
        else:
            # Invalid input, prompt again
            print(f"\nInvalid choice. Please select ({config.Fore.GREEN}1{config.Style.RESET_ALL} /{config.Fore.BLUE} 2 {config.Style.RESET_ALL}/ {config.Fore.LIGHTRED_EX}3{config.Style.RESET_ALL})")
            
    return difficulty
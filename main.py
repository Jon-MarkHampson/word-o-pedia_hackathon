import grid_utils
import word_utils
import config
import hints
import terminal_timer
import leader_board
import grid_style
import time

def main():
    """ Main function to run the game """
    
    #Initialise counters
    colours_counter = 0
    found_words_counter = 0
    hint_counter = 0
    penalty_counter = 0
    penalty_time = 15

    #Initialise an instance of the SimpleTimer
    timer = terminal_timer.SimpleTimer()
    timer.start()
    
    #Print HEADER / ASCII ART??

    #Print game info/ how to play ??
    
    
    # Prompt user for their name
    player_name = input("\nPlease enter your name: ").strip() # Need use this to add to leaderboard

    # Print the leaderboard?
    
    #Print / Select Difficulty
    print("\n1. Easy\n2. Medium\n3. Hard")
    choice = input(f"\nPlease choose your level of Difficulty (1, 2, 3): ").strip() 
    difficulty = {
        "1": config.EASY,
        "2": config.MEDIUM,
        "3": config.HARD
    }.get(choice)

    grid_size, num_words = difficulty # eg difficulty = (10, 7) because congfig.MEDIUM = (10, 7)

    # Prompt user for a topic
    user_topic = word_utils.get_game_topic()
    
    # Get links from the Wikipedia page and filter game words
    links = word_utils.get_links_from_wiki(user_topic)
    game_words = word_utils.filter_game_words(links, grid_size, num_words)
    
    # print(f"DEBUG game_wrods: {game_words})")
    
    if not game_words:
        print("\nGame cannot proceed due to lack of valid words.")
        return
    
    #Init and create game grid using words from above
    game_grid, words_positions = grid_utils.initialise_game_grid(grid_size, game_words)
    
    # print(words_positions)
    print("\nHere is your WORD-O-PEDIA - GOOD LUCK!:\n")
    
    while found_words_counter < num_words:
        # print("\nHere is your game grid:\n")
        grid_utils.print_grid(game_grid)
        #Display current elapsed time
        timer.display()
        print("Penalty Time: " + config.Fore.RED + f"{penalty_counter}" + config.Style.RESET_ALL + " seconds")
        
        # Ask for user input. Check if the user wants a hint
        want_hint = input("\nWould you like a hint? (Y / N): ").strip().lower()
        # Always get the first word in the remaining game_words list
        if want_hint in {"y", "yes", "yeah"}: 
            
            # Get a hint about the word
            if hint_counter == 0:
                hint = hints.get_hint_about_word(game_words[0], hint_counter)
            
            # Update hint counter and penalty counter 
            hint_counter += 1
            penalty_counter += penalty_time
            
            print(f"\nPENALTY: {config.Fore.RED + str(penalty_counter) + config.Style.RESET_ALL} seconds added to your time.")
            
            # print("\nDEBUG: ", games_words[0])
            print(f"\nYou are looking for a word with {len(game_words[0])} characters.\n")
            
            # Get the revealed part of the word
            revealed_part = hints.reveal_the_word(game_words[0], hint_counter)
            
            print(f"\n\t\t{revealed_part}\n")
            print(f"\n{hint}\n")
            
            
        user_guess = input("\nEnter a found word: ").strip().lower()
        if user_guess in game_words:
            print("\nWHOOOOOOOOO! You found " + config.COLOURS_LIST[colours_counter] + user_guess + config.Style.RESET_ALL + "\n")
            grid = grid_utils.update_game_grid(game_grid, user_guess, colours_counter, words_positions)
            colours_counter += 1  # Update colour counter so next guessed word gets a different colour
            found_words_counter += 1  # Update the found words counter
            hint_counter = 0  # Update which word to provide hints for
            game_words.remove(user_guess)
        else:
            print(f"\n{config.Fore.RED + user_guess + config.Style.RESET_ALL} isn't one of the words we are looking for.\n")


    timer.stop()
    grid_utils.print_grid(game_grid)
    # final_time, min, sec = timer.return_elapsed_time()

    # total_time = final_time + penalty_counter
    # minutes = int(total_time // 60)
    # seconds = int(total_time % 60)  
    
    #End the game and stop the timer
    # timer.stop()

    # Calculate final time including penalty
    total_time = time.time() - timer.start_time + penalty_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)

    # Display the results
    print("\nGame over! All words found.")
    print(f"Total time with penalty: {minutes:02d}:{seconds:02d} (Penalty: {penalty_time} seconds)")

    print(f"You found all {len(num_words)} words in: {minutes}:{seconds} ")
    #add username and final time to high score leaderboard?



if __name__ == "__main__":
    main()

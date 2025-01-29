import grid_utils
import word_utils
import config
import hints
import terminal_timer
from leader_board import Leaderboard
import time
import game
import print_game_info

def main():
    """ Main function to run the game """
    
    leader_board = Leaderboard()
    
    #Initialise counters
    colours_counter = 0
    found_words_counter = 0
    hint_counter = 0
    penalty_counter = 0
    penalty_time = 15

    #Initialise an instance of the SimpleTimer
    timer = terminal_timer.SimpleTimer()
    timer.start()

    print_game_info.print_game_info()
    
    
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

    grid_size, num_words , diff_string = difficulty # eg difficulty = (10, 7, EASY) because congfig.MEDIUM = (10, 7, EASY)

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
    print(f"\nHere is your {config.Fore.BLUE}WORD-O-PEDIA{config.Style.RESET_ALL} - GOOD LUCK {config.Fore.GREEN}{player_name}{config.Style.RESET_ALL}!:\n")
    
    while found_words_counter < num_words:
        # print("\nHere is your game grid:\n")
        grid_utils.print_grid(game_grid)
        #Display current elapsed time
        print(f"You have {config.Fore.MAGENTA}{num_words - found_words_counter}{config.Style.RESET_ALL} words left to find.\n")
        timer.display()
        print(f"Penalty Time: {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL} seconds")
        
        # Ask for user input. Check if the user wants a hint
        user_guess_word = input("\nWould you like a hint? (Type 'hint') - Or enter your guess now: ").strip().lower()
            
        # Always get the first word in the remaining game_words list
        if user_guess_word in game_words:
            game_words, game_grid, found_words_counter, colours_counter = game.check_if_word_in_game_words(user_guess_word, game_words, game_grid, words_positions, found_words_counter, colours_counter)
            continue
        elif user_guess_word == "hint": 
            
            # Get a hint about the word
            if hint_counter == 0:
                hint = hints.get_hint_about_word(game_words[0])
            
            # Update hint counter and penalty counter 
            hint_counter += 1
            penalty_counter += penalty_time
            
            print(f"\nPENALTY: {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL} seconds added to your time.")
            
            # print("\nDEBUG: ", games_words[0])
            print(f"\nYou are looking for a word with {len(game_words[0])} characters.\n")
            
            # Get the revealed part of the word
            revealed_part = hints.reveal_the_word(game_words[0], hint_counter)
            
            print(f"\n\t\t{revealed_part}\n")
            print(f"\n{hint}\n")
                        
        else:
            print(f"\n{config.funny_negative_responses_prefix[hint_counter]} {config.Fore.RED}{user_guess_word}{config.Style.RESET_ALL} isn't one of the words we are looking for. {config.funny_negative_responses_suffix[hint_counter]}\n")

    # Stop timer
    timer.stop()
    
    # Display the final grid
    grid_utils.print_grid(game_grid)

    # Calculate final time including penalty
    total_time = time.time() - timer.start_time + penalty_time
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)

    # Display the results
    print("\nGAME OVER!")
    
    print("\nALL WORDS FOUND!\n")

    print(f"\nTotal time with penalty: {minutes:02d}:{seconds:02d} (Penalty: {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL} seconds)")

    print(f"\nYou found all {config.Fore.CYAN}{num_words}{config.Style.RESET_ALL} words in: {config.Fore.YELLOW}{minutes}:{seconds}{config.Style.RESET_ALL}")
    
    #add username and final time to high score leaderboard?
    leader_board.update_leaderboard(player_name, diff_string, total_time)
    leader_board.display_leaderboard()
    
    print(f"\nThank you {player_name} for playing WORD-O-PEDIA!\n")
    
    print("Heres is a summary about the words we found and how they relate to the topic you chose:\n")



if __name__ == "__main__":
    main()

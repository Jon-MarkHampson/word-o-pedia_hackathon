""" Main module to run the game """

import grid_utils
import word_utils
import config
import hints
import terminal_timer
import time
import game
import difficulty_level
import print_game_info
from leader_board import Leaderboard


def main():
    """ Main function to run the game """
    
    # Initialise the Leaderboard Class
    leader_board = Leaderboard()
    
    while True:
        """ We need to initialise the game grid, get the user's name, topic, and difficulty level, and then start the game """
        
        #Initialise counters
        colours_counter = 0
        found_words_counter = 0
        hint_counter = 0
        penalty_counter = 0
        penalty_time = 15

        #Initialise an instance of the SimpleTimer Class
        timer = terminal_timer.SimpleTimer()

        print_game_info.print_game_info()
                
        # Prompt user for their name
        player_name = input("\nPlease enter your name: ").strip()

        leader_board.display_leaderboard()
        
        difficulty = difficulty_level.set_difficulty()

        # Unpacking difficulty tuple eg difficulty = (10, 7, EASY)
        grid_size, num_words, difficulty_string = difficulty 

        # Prompt user for a topic
        user_topic = word_utils.get_game_topic()
        
        # Get links from the Wikipedia page and filter game words
        links = word_utils.get_links_from_wiki(user_topic)
        game_words = word_utils.filter_game_words(links, grid_size, num_words)
        
        # Create a summary for the user about how the words relate to the topic
        summaries = hints.generate_summaries_for_all_game_words(game_words, user_topic)
        
        # Check if there are any valid words to play the game
        if not game_words:
            print("\nERROR: Game cannot proceed due to lack of valid words.")
            continue
        
        # Initialise the game grid
        game_grid, words_positions, unplaced_words = grid_utils.initialise_game_grid(grid_size, game_words)

        for word in unplaced_words:
            game_words.remove(word)
            print(f"\n{config.Fore.LIGHTRED_EX}WARNING - YOU GOT LUCKY!:{config.Style.RESET_ALL} The word '{config.Fore.LIGHTRED_EX}{word}{config.Style.RESET_ALL}' was unfortunatley not placed in the grid and has been removed from the game.")
            num_words -= 1
        
        # print(words_positions)
        print(f"\nHere is your {config.Fore.BLUE}WORD-O-PEDIA{config.Style.RESET_ALL} - GOOD LUCK {config.Fore.GREEN}{player_name}{config.Style.RESET_ALL}!:\n")
        
        # Start the timer
        timer.start()
        
        # Main game loop
        while found_words_counter < num_words:
            # print("\nHere is your game grid:\n")
            grid_utils.print_grid(game_grid)
            
            # Display the number of words left to find
            print(f"You have {config.Fore.MAGENTA}{num_words - found_words_counter}{config.Style.RESET_ALL} words left to find.\n")
            
            #Display current elapsed time and penalty time
            timer.display()
            print(f"Penalty Time: {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL} seconds")
            
            # Ask for user input. Check if the user wants a hint
            user_guess_word = input("\nWould you like a hint? (Type 'H') - Or enter your guess now: ").strip().lower()
                
            # Check if the user's guess is in the game words
            if user_guess_word in game_words:
                game_words, game_grid, found_words_counter, colours_counter = game.check_if_word_in_game_words(user_guess_word, game_words, game_grid, words_positions, found_words_counter, colours_counter)
                hint_counter = 0
                continue
            
            # Check if the user wants a hint
            elif user_guess_word == "h": 
                
                # Get a hint about the word from chatGTP API call only if hint_counter is 0
                if hint_counter == 0:
                    hint = hints.get_hint_about_word(game_words[0])
                
                # Update hint counter and penalty counter 
                hint_counter += 1
                penalty_counter += penalty_time
                
                print(f"\nPENALTY: {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL} seconds added to your time.")
                
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
        leader_board.update_leaderboard(player_name, difficulty_string, total_time)
        leader_board.display_leaderboard()
        
        print(f"\nThank you {config.Fore.GREEN}{player_name}{config.Style.RESET_ALL} for playing {config.Fore.CYAN}WORD-O-PEDIA!{config.Style.RESET_ALL}\n")
        
        print("Here is a summary about the words we found and how they relate to the topic you chose:\n")
        
        hints.print_summaries(summaries)
            

        end_game = input("Would you like to play again? (Y / N): ").strip().lower()
        if end_game in {"y", "yes", "yeah", "yep"}:
            continue
        else:
            print("\nGoodbye!")
            return
    

if __name__ == "__main__":
    main()

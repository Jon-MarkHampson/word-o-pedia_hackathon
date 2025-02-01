""" Main module to run the game """
import sys
import grid_utils
import word_utils
import config
import hints
import game
import difficulty_level
import print_game_info
import stopwatch
from leader_board import Leaderboard
from colorama import Fore, Style



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
        
        # Initialize the stopwatch and set its position on the screen
        game_stopwatch = stopwatch.Stopwatch()
        game_stopwatch.set_timer_position_to_second_to_last_line()  # Timer on second-to-last line
        game_stopwatch.set_input_position_to_last_line()  # Set input prompt position on last line

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
            print(f"\n{Fore.LIGHTRED_EX}WARNING - YOU GOT LUCKY!:{Style.RESET_ALL} The word '{Fore.LIGHTRED_EX}{word}{Style.RESET_ALL}' was unfortunatley not placed in the grid and has been removed from the game.")
            num_words -= 1
        
        # print(words_positions)
        print(f"\nHere is your {Fore.BLUE}WORD-O-PEDIA{Style.RESET_ALL} - GOOD LUCK {Fore.GREEN}{player_name}{Style.RESET_ALL}!:\n")

        # Start the stopwatch
        game_stopwatch.start()    
         
        # Main game loop
        while found_words_counter < num_words:

            grid_utils.print_grid(game_grid)
            
            # Display the number of words left to find
            print(f"You have {Fore.MAGENTA}{num_words - found_words_counter}{Style.RESET_ALL} words left to find.\n")
            
            # Display the penalty time if any
            print(f"Penalty Time: {Fore.LIGHTRED_EX}{penalty_counter}{Style.RESET_ALL} seconds")
            
            # Move cursor to the last line, col 1, clear it, then prompt
            prompt_row = game_stopwatch.input_prompt_position
            
            # Ask for user input. Check if the user wants a hint.
            user_guess_word = input("\nWould you like a hint? (Type 'H') - Or enter your guess now: ").strip().lower()        
            
            # Stop the stopwatch while checking the user input and getting the hint
            game_stopwatch.pause()               
                
            # Check if the user's guess is in the game words
            if user_guess_word in game_words:
                game_words, game_grid, found_words_counter, colours_counter = game.check_if_word_in_game_words(user_guess_word, game_words, game_grid, words_positions, found_words_counter, colours_counter)
                hint_counter = 0
                # Clear the screen
                # grid_utils.clear_screen()
            
            # Check if the user wants a hint
            elif user_guess_word == "h": 
                
                # Get a hint about the word from chatGTP API call only if hint_counter is 0
                if hint_counter == 0:
                    hint = hints.get_hint_about_word(game_words[0])
                
                # Update hint counter and penalty counter 
                hint_counter += 1
                penalty_counter += penalty_time
                # Clear the screen
                # grid_utils.clear_screen()
                
                print(f"\nPENALTY: {Fore.RED}{penalty_counter}{Style.RESET_ALL} seconds added to your time.")
                
                print(f"\nYou are looking for a word with {config.COLOURS_LIST[found_words_counter]}{len(game_words[0])}{Style.RESET_ALL} characters.\n")
                
                # Get the revealed part of the word
                revealed_part = hints.reveal_the_word(game_words[0], hint_counter)
                
                print(f"\n\t\t{config.COLOURS_LIST[found_words_counter]}{revealed_part}{Style.RESET_ALL}\n")
                print(f"\n{hint}\n")
                            
            else:
                print(f"\n{config.funny_negative_responses_prefix[hint_counter]} {Fore.RED}{user_guess_word}{Style.RESET_ALL} isn't one of the words we are looking for. {config.funny_negative_responses_suffix[hint_counter]}\n")
                # Clear the screen
                # grid_utils.clear_screen()

            # Resume and display the stopwatch
            game_stopwatch.resume()
                
        # Stop stopwatch
        game_stopwatch.stop()
        
        # Display the final grid
        grid_utils.print_grid(game_grid)

        # Calculate final time including penalty
        total_time = game_stopwatch.elapsed_time + penalty_counter
        # total_time = time.time() - timer.start_time + penalty_counter
        minutes = int(total_time // 60)
        seconds = int(total_time % 60)

        # Display the results
        print("\nGAME OVER!")
        
        print("\nALL WORDS FOUND!\n")

        print(f"\nTotal time with penalty: {minutes:02d}:{seconds:02d} (Penalty: {Fore.RED}{penalty_counter}{Style.RESET_ALL} seconds)")

        print(f"\nYou found all {Fore.CYAN}{num_words}{Style.RESET_ALL} words in: {Fore.YELLOW}{minutes}:{seconds}{Style.RESET_ALL}")
        
        #add username and final time to high score leaderboard?
        leader_board.update_leaderboard(player_name, difficulty_string, total_time)
        leader_board.display_leaderboard()
        
        print(f"\nThank you {Fore.GREEN}{player_name}{Style.RESET_ALL} for playing {Fore.CYAN}WORD-O-PEDIA!{Style.RESET_ALL}\n")
        
        print("Here is a summary about the words we found and how they relate to the topic you chose:\n")
        
        hints.print_summaries(summaries)
            

        end_game = input("Would you like to play again? (Y / N): ").strip().lower()
        if end_game in {"y", "yes", "yeah", "yep"}:
            continue
        else:
            print(f"\nThanks for playing {Fore.BLUE}WORD-O-PEDIA! {Style.RESET_ALL}Goodbye!\n")
            return
    

if __name__ == "__main__":
    main()

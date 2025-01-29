"""
Main game logic that ties everything together
"""
import config
import grid_utils

def check_if_word_in_game_words(word, game_words, game_grid, words_positions, found_words_counter, colours_counter):
    """Check if a word is in the game words list."""
    if word in game_words:
        print(f"\n{config.funny_positive_responses[found_words_counter]} You found {config.COLOURS_LIST[colours_counter]}{word.upper()}{config.Style.RESET_ALL}\n")
        grid = grid_utils.update_game_grid(game_grid, word, colours_counter, words_positions)
        colours_counter += 1 # Update colour counter so next guessed word gets a different colour
        if colours_counter == len(config.COLOURS_LIST):
            colours_counter = 0
        found_words_counter += 1  # Update the found words counter
        hint_counter = 0  # Update which word to provide hints for
        game_words.remove(word)
    return game_words, game_grid, found_words_counter, colours_counter
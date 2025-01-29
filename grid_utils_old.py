"""
Functions for creating and managing the word search grid.
Handles word placement and grid operations.
"""
import random
import re
from colorama import Fore, Style
import config

def fill_grid_with_placeholders(grid_size):
    """Creates a grid filled with '*' placeholders."""
    return [["*" for _ in range(grid_size)] for _ in range(grid_size)]


def try_place_word(grid, word, row, col, horizontal):
    """
    Attempts to place a word on the grid starting at (row, col).
    Returns True if successful, False otherwise.
    """
    length = len(word)
    if horizontal:
        if col + length > len(grid[0]):  # Check horizontal bounds
            return False
        if all(grid[row][col + i] not in ("*", word[i]) for i in range(length)):
            return False
        for i in range(length):
            grid[row][col + i] = word[i]
    else:
        if row + length > len(grid):  # Check vertical bounds
            return False
        if all(grid[row + i][col] not in ("*", word[i]) for i in range(length)):
            return False
        for i in range(length):
            grid[row + i][col] = word[i]
    return True


def place_words_on_grid(grid, words):
    """Places words randomly on the grid."""
    grid_size = len(grid)
    words_positions = {}  # <-- new dictionary to store the placed coordinates

    for word in words:
        word = word.upper()
        placed = False

        for _ in range(100):
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            horizontal = random.choice([True, False])

            # Try placing the word
            if try_place_word(grid, word, row, col, horizontal):
                # If successful, gather and store the coordinates for this word
                coordinates = [] # Create an empty list to store the coordinates
                length = len(word)
                if horizontal:
                    for i in range(length):
                        coordinates.append((row, col + i))
                else:  # vertical
                    for i in range(length):
                        coordinates.append((row + i, col))

                words_positions[word] = coordinates # add the word coordinates to each word
                placed = True
                break

        if not placed:
            print(f"Warning: Could not place the word '{word}' on the grid.")

    return grid, words_positions # returning a tuple


def fill_placeholders_with_random_letters(grid):
    """Replaces all '*' placeholders in the grid with random letters."""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "*":
                grid[row][col] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return grid


def print_grid(grid):
    """Prints the grid with tabs between letters for better readability."""
    print("\n")
    for row in grid:
        print("\t".join(row)+("\n" * 2))
    print("\n")

def initialise_game_grid(grid_size, words):
    """Initialises the game grid with words placed randomly."""
    grid = fill_grid_with_placeholders(grid_size)
    grid = place_words_on_grid(grid, words)
    # print = grid
    # grid = fill_placeholders_with_random_letters(grid)
    return grid

def update_game_grid(grid, word, colours_counter, words_positions):
    # 'word' is uppercase in the puzzle
    word = word.upper()

    # Retrieve the list of coordinates from the dictionary
    coordinates = words_positions.get(word, [])

    # Color each character at those coordinates
    for (r, c) in coordinates:
        original_char = grid[r][c]
        # Remove any existing color codes if you prefer, or just color over it
        # For safety, remove ANSI codes so we don't get nested codes
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        plain_char = ansi_escape.sub('', original_char)

        grid[r][c] = (config.COLOURS_LIST[colours_counter]
                                  + plain_char
                                  + Style.RESET_ALL)

    return grid
import random
import re
from colorama import Fore, Style
import config

def fill_grid_with_placeholders(grid_size):
    """Creates a grid filled with '*' placeholders."""
    return [["*" for _ in range(grid_size)] for _ in range(grid_size)]

def try_place_word(grid, word, row, col, horizontal, reverse):
    """
    Attempts to place a word on the grid starting at (row, col).
    Returns True if successful, False otherwise.
    """
    length = len(word)
    if reverse:
        word = word[::-1]  # Reverse the word if needed

    if horizontal:
        if col + length > len(grid[0]):  # Check horizontal bounds
            return False
        for i in range(length):
            if grid[row][col + i] not in ("*", word[i]):
                return False
        for i in range(length):
            grid[row][col + i] = word[i]
    else:  # Vertical
        if row + length > len(grid):  # Check vertical bounds
            return False
        for i in range(length):
            if grid[row + i][col] not in ("*", word[i]):
                return False
        for i in range(length):
            grid[row + i][col] = word[i]
    
    return True

def place_words_on_grid(grid, words):
    """Places words randomly on the grid, allowing reverse placement."""
    grid_size = len(grid)
    words_positions = {}  # Dictionary to store the placed coordinates

    for word in sorted(words, key=len, reverse=True):  # Place longer words first
        word = word.upper()
        placed = False

        for _ in range(100):  # Try up to 100 times for each word
            row = random.randint(0, grid_size - 1)
            col = random.randint(0, grid_size - 1)
            horizontal = random.choice([True, False])
            reverse = random.choice([True, False])

            # Try placing the word
            if try_place_word(grid, word, row, col, horizontal, reverse):
                coordinates = []  # Store the coordinates of the placed word
                length = len(word)
                if horizontal:
                    for i in range(length):
                        coordinates.append((row, col + i))
                else:  # Vertical
                    for i in range(length):
                        coordinates.append((row + i, col))

                words_positions[word] = coordinates
                placed = True
                break

        if not placed:
            print(f"Warning: Could not place the word '{word}' on the grid.")

    return grid, words_positions  # Return the updated grid and word positions

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
        print("\t".join(row) + ("\n" * 2))
    print("\n")

def initialise_game_grid(grid_size, words):
    """Initialises the game grid with words placed randomly."""
    grid = fill_grid_with_placeholders(grid_size)
    grid, words_positions = place_words_on_grid(grid, words)
    grid = fill_placeholders_with_random_letters(grid)
    return grid, words_positions

def update_game_grid(grid, word, colours_counter, words_positions):
    """Highlights a word on the grid by colouring its letters."""
    word = word.upper()
    coordinates = words_positions.get(word, [])

    for (r, c) in coordinates:
        original_char = grid[r][c]
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        plain_char = ansi_escape.sub('', original_char)

        grid[r][c] = (config.COLOURS_LIST[colours_counter] + plain_char + Style.RESET_ALL)

    return grid

# Example usage:
if __name__ == "__main__":
    grid_size = 10
    words = ["PYTHON", "GAME", "CODE", "SEARCH", "GRID", "WORD"]

    grid, words_positions = initialise_game_grid(grid_size, words)
    print_grid(grid)

    # Example of highlighting a word
    colours_counter = 0
    update_game_grid(grid, "PYTHON", colours_counter, words_positions)
    print_grid(grid)

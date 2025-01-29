from colorama import Back, Fore, Style

def print_grid(grid):
    """
    Prints the grid with a retro-style black background and vibrant text colors.
    """
    print("\n")
    for row in grid:
        styled_row = "\t".join(
            f"{Back.BLACK}{Fore.CYAN}{cell}{Style.RESET_ALL}" for cell in row
        )
        print(styled_row)
        print("\n")  # Add spacing for better readability
    print("\n")
"""
Contains basic game settings and configurations. 
Keeps constants in one place for easy updates.
"""
from colorama import Fore, Style

# Difficulty levels: (grid size, number of words)
EASY = (7, 5, "EASY")
MEDIUM = (10, 7, "MEDIUM")
HARD = (15, 10, "HARD")

WIKI_LANGUAGE = "en"

# Colour constants
COLOURS_LIST = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# Funny responses for found words
funny_positive_responses = ["You're on fire!",
                            "You're a word wizard!",
                            "You're a word ninja!",
                            "You're a word-finding machine!",
                            "You're a word genius!",
                            "You're a word master!",
                            "You're a word champion!",
                            "You're a word superstar!",
                            "You're a word hero!",
                            "You're a word legend!"]
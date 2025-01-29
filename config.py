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
COLOURS_LIST = [Fore.MAGENTA, Fore.GREEN, Fore.BLUE, Fore.RED, Fore.CYAN, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTCYAN_EX]

# Funny responses for found words
funny_positive_responses = [
    "You're on fire!",
    "You're a word wizard!",
    "You're a word ninja!",
    "You're a word-finding machine!",
    "You're a word genius!",
    "You're a word master!",
    "You're a word champion!",
    "You're a word superstar!",
    "You're a word hero!",
    "You're a word legend!"
    ]

funny_negative_responses_prefix = [
    "Bzzt! Wrong!",
    "Swing and a miss!",
    "No luck!",
    "That ain't it!",
    "Sad trombone!",
    "Yikes!",
    "Denied!",
    "Womp womp!",
    "Oh dear!",
    "That's a nope!",
]

funny_negative_responses_suffix = [
    "Stay positive, you've got this!"
    "Maybe ask for a hint!",
    "You're learning—keep going!",
    "You can do it!",
    "Don't give up!",
    "Take a deep breath and try again!",
    "I believe in you!",
    "Maybe ask for a hint!",
    "Stay determined!",
    "Keep pushing forward!"
]



""" Print the Title of the Game and the Difficulty and the Descriptiomn of the Game """

from colorama import Fore, Style

config.COLOURS_LIST

# print(Fore.RED + "This text is red!" + Style.RESET_ALL)
# COLOURS_LIST = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]


def print_game_info():
    print("Welcome to WORD-O-PEDIA!")
    # ACSII Art?
    # Game Description

    print(f""""
                       ,,,,,,,,,,,,,,       ,,,,,,,,,,,,,,,....
                .****,,,,,,,,,,,,,,,         ,,,,,,,,,,,,,,,,.....
                 ******,,,,,,,,,,              ,,,,,,,,,,,,,,,,,.
                  ******,*,,,,,,                 ,,,,,,,,,,,,,,.
                  **********,,,,,               ,,,,,,,,,,,,,,,,,
                   ************,,,             ,,,,,,,,,,,,,,,,,
                   *************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                  ****************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
     ******,      ********************,,,,,,,,,,,,,,,,,,,,,,,,,,        ,,,,,,.
 *******************                                        ,,,,,,,,,,,,,,,,,,,,
 /****************@.     WORD-O-PEDIA By Ctrl Alt Elite     ,,,,,,,,,,,,,,,,,,,,,
////***************                                          ,,,,,,,,,,,,,,,,,,,
 //////****************************************,,,,,,,,,,,,,,,,,,,    ,,,,,,,,,
 ///////****   *********************************,*,,,,,,,,,,,,,,,       ,,,,,
   //////        ***********************************,,,,,,,,,,,,
                 ***********************************,,,,,,,,,,,,
                 ****************               *********,,,,,,,
                 //************                  **********,,,,,
                 ////***********                 *************,,,
                 //////************            *****************,
                /////////************       *****************
                     /////////********     ****************
""")



    print(f"""
    
        GAME DESCRIPTION:
    
    * This is a word search game
    * Words are taken from a Wikipedia article on a topic of your choice or randomly
    * A character matrix hides the words
    * You can choose the size of matrix (the level of difficulty)
    * Correctly found words will be color highlighted
    * Leaderboard: all words found in fastest time
    
    
     GAME RULES:
    
    * Keep on guessing and typing words until you find all the correct words
    * Choice of getting a hint
    * Optional timer for competitive players
    * Game stops when all words are found
""")
    
    print(f"\nDifficulty: Grid size {grid_size}x{grid_size}, {num_words} words to find.")

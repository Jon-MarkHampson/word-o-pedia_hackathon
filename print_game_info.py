""" Print the Title of the Game and the Difficulty and the Descriptiomn of the Game """

from colorama import Fore, Style

config.COLOURS_LIST

# print(Fore.RED + "This text is red!" + Style.RESET_ALL)
# COLOURS_LIST = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
# {config.Fore.RED}{penalty_counter}{config.Style.RESET_ALL}


def print_game_info():
    print("Welcome to WORD-O-PEDIA!")
    # ACSII Art?
    # Game Description

    print(f""""
    {config.Fore.YELLOW}
                     ,,,,,,,,,,,,,,,,       ,,,,,,,,,,,,,,,....
                *****,,,,,,,,,,,,,,          ,,,,,,,,,,,,,,,,.....
                 ******,,,,,,,,,,              ,,,,,,,,,,,,,,,,..
                  *******,,,,,,,                ,,,,,,,,,,,,,,.
                  **********,,,,,               ,,,,,,,,,,,,,,,,,
                   ************,,,             ,,,,,,,,,,,,,,,,,
                   *************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                  ****************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
     *******      ********************,,,,,,,,,,,,,,,,,,,,,,,,,,,,      ,,,,,,,
 *******************                                        ,,,,,,,,,,,,,,,,,,,,,
/******************      WORD-O-PEDIA By Ctrl Alt Elite      ,,,,,,,,,,,,,,,,,,,,,
////***************                                          ,,,,,,,,,,,,,,,,,,,,
 //////****************************************,,,,,,,,,,,,,,,,,,,    ,,,,,,,,,,
 ///////****   **********************************,,,,,,,,,,,,,,,,       ,,,,,
   //////        ***********************************,,,,,,,,,,,,
                 *************************************,,,,,,,,,,,
                 ****************               *********,,,,,,,
                 //************                  **********,,,,,
                 ////***********                 *************,,,
                 //////************            *****************,
                /////////************       *******************
                     /////////********     ****************
{config.Style.RESET_ALL}""")



    print(f"""
    {config.Fore.CYAN}
        GAME DESCRIPTION:{config.Style.RESET_ALL}
    
    {config.Fore.YELLOW}
    * This is a word search game based on Wikipedia which helps you learn about various topics as you play :)
    * Words are taken from a Wikipedia article on a topic of your choice or randomly
    * A character matrix hides the words
    * You can choose the size of matrix (the level of difficulty)
    * Correctly found words will be color highlighted
    * The words can be displayed either HORIZONTAL, VERTICAL or BACKWARDS (for both) 
    * Leaderboard: all words found in fastest time{config.Style.RESET_ALL}
    
    
    {config.Fore.CYAN}
     GAME RULES:{config.Style.RESET_ALL}
    
    {config.Fore.YELLOW}
    * Keep on guessing and typing words until you find all the correct words
    * Choice of getting a hint
    * You can also type "hint" if you missed the choice and feel lost
    * You have a timer - to make it more competitive ;)
    * You get a 15 sec penalty for every hint
    * Game stops when all words are found
{config.Style.RESET_ALL}""")
    
    print(f"\nDifficulty: Grid size {grid_size}x{grid_size}, {num_words} words to find.")

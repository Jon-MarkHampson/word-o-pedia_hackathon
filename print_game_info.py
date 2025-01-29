""" Print the Title of the Game and the Difficulty and the Descriptiomn of the Game """
import config

def print_game_info():
    print(f"""
    
    {config.Fore.CYAN}
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
/******************      {config.Fore.LIGHTYELLOW_EX}WORD-O-PEDIA By Ctrl Alt Elite{config.Style.RESET_ALL}      ,,,,,,,,,,,,,,,,,,,,,
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
    {config.Fore.LIGHTYELLOW_EX}
    * This is a word search game based on Wikipedia which helps you learn about various topics as you play :)
    * Words are taken from a Wikipedia article on a topic of your choice or randomly.
    * A grid of letters hides the words.
    * You can choose the diffuculty which will set the size of the game and the number of words to find.
    * Correctly found words will be color highlighted.
    * The words can be displayed either HORIZONTAL, VERTICAL or BACKWARDS (for both). 
    * Leaderboard: All words found in fastest time.{config.Style.RESET_ALL}
    
    {config.Fore.CYAN}
    GAME RULES:{config.Style.RESET_ALL}  
    {config.Fore.LIGHTYELLOW_EX}
    * Keep on guessing and typing words until you find all the correct words.
    * You have a timer - to make it more competitive ;)
    * You can type "hint" if you feel lost.
    * You get a 15 sec penalty for every hint.
    * Game stops when all words are found.
{config.Style.RESET_ALL}""")

import time
import config




class SimpleTimer():
    def __init__(self):
        """Initialize a basic timer that tracks elapsed time."""
        self.start_time = None
        self.is_running = False


    def start(self):
        """Start the timer by recording the current time."""
        self.start_time = time.time()
        self.is_running = True


    def stop(self):
        """Stop the timer."""
        self.stop_time = time.time()
        self.is_running = False


    # def return_elapsed_time(self):
    #     """Return the current elapsed time in the terminal."""
    #     if not self.is_running:
    #         return
        
    #     elapsed_time = time.time() - self.start_time
    #     minutes = int(elapsed_time // 60)
    #     seconds = int(elapsed_time % 60)
    #     return minutes, seconds
        

    def display(self):
        """Display the current elapsed time in the terminal."""
        if not self.is_running:
            return
        
        elapsed_time = time.time() - self.start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        print(f"Elapsed Time: {config.Fore.RED}{minutes:02d}:{seconds:02d}{config.Style.RESET_ALL}")


# # The game function JUST an example to test
# def start_game():
#     words_to_find = ["apple", "banana", "cherry", "date", "elderberry"]
#     found_words = []

#     # Create an instance of the SimpleTimer
#     timer = SimpleTimer()

#     # Start the timer
#     timer.start()
#     print("Game started! Start typing words to find.")

#     # Game loop
#     while len(found_words) < len(words_to_find):
#         # Display current found words
#         print("\nFound words:", found_words)

#         # Prompt user for word input
#         word = input("Enter a word: ").strip().lower()

#         # Check if the word is correct
#         if word in words_to_find and word not in found_words:
#             found_words.append(word)
#             print(f"Correct! {word} found.")
#         else:
#             print(f"'{word}' is either not correct or already found.")

#         # Display timer every time user enters a word
#         timer.display()

#     # End the game and stop the timer
#     timer.stop()
#     print("\nGame over! All words found.")

#     # Calculate and display the final time
#     print(
#         f"Total time: {int((time.time() - timer.start_time) // 60)} minutes and {int((time.time() - timer.start_time) % 60)} seconds.")


# # Start the game
# start_game()

#   # End the game and stop the timer
#     timer.stop()

#     # Calculate final time including penalty
#     total_time = time.time() - timer.start_time + penalty_time
#     minutes = int(total_time // 60)
#     seconds = int(total_time % 60)

#     # Display the results
#     print("\nGame over! All words found.")
#     print(f"Total time with penalty: {minutes:02d}:{seconds:02d} (Penalty: {penalty_time} seconds)")

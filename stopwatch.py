import time
import threading
import sys
import shutil
from colorama import Fore, Style

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.running = False
        self.elapsed_time = 0  # total elapsed time so far (in seconds)

        self._lock = threading.Lock()
        
        # Timer position defaults
        self.timer_position = (1, 1)       # second-to-last line
        self.input_prompt_position = None  # last line

    def _get_terminal_height(self):
        size = shutil.get_terminal_size()
        return size.lines

    def set_timer_position_to_second_to_last_line(self):
        h = self._get_terminal_height()
        row = max(1, h - 1)
        self.timer_position = (row, 1)

    def set_input_position_to_last_line(self):
        h = self._get_terminal_height()
        self.input_prompt_position = max(1, h)

    def _move_cursor_to_position(self, row, column):
        sys.stdout.write(f"\033[{row};{column}H")

    def _clear_line(self):
        """Clear from cursor to end of line."""
        sys.stdout.write("\033[K")

    def _clear_timer_line(self):
        """
        Go to the timer line, clear it, then restore the cursor.
        This makes the timer line effectively 'disappear'.
        """
        # Save cursor
        sys.stdout.write("\0337")
        sys.stdout.flush()

        # Move to timer line
        row, col = self.timer_position
        self._move_cursor_to_position(row, col)
        self._clear_line()

        # Restore cursor
        sys.stdout.write("\0338")
        sys.stdout.flush()

    def _print_time(self):
        """
        Print the timer at its position, using save/restore so we
        don't break the user's prompt line.
        """
        with self._lock:
            if self.running:
                current_time = time.time() - self.start_time + self.elapsed_time
            else:
                # If it's not running, we show nothing. But let's return early
                # so we don't clutter the line.
                return

        minutes, seconds = divmod(int(current_time), 60)

        # Save cursor
        sys.stdout.write("\0337")
        sys.stdout.flush()

        # Move to timer position
        row, col = self.timer_position
        self._move_cursor_to_position(row, col)
        self._clear_line()

        # Print the timer
        sys.stdout.write(
            f"Timer: {Fore.LIGHTRED_EX}{minutes:02}{Style.RESET_ALL}"
            f":{Fore.LIGHTRED_EX}{seconds:02}{Style.RESET_ALL}"
        )
        sys.stdout.flush()

        # Restore cursor
        sys.stdout.write("\0338")
        sys.stdout.flush()

    def display(self):
        """Continuously update the timer until self.running=False."""
        while True:
            with self._lock:
                # If the stopwatch is no longer running, exit the loop
                if not self.running:
                    break

            # Recalc positions in case terminal resized
            self.set_timer_position_to_second_to_last_line()
            self._print_time()
            time.sleep(1)

    def start(self):
        """
        Start the stopwatch from zero or after a full stop.
        If you want to continue from a partial pause, see resume().
        """
        with self._lock:
            # Reset everything to zero for a fresh start
            self.elapsed_time = 0
            self.start_time = time.time()
            self.running = True
        
        self._thread = threading.Thread(target=self.display, daemon=True)
        self._thread.start()

    def stop(self):
        """
        Stop the stopwatch entirely.
        This is 'game over' - final result is stored in self.elapsed_time.
        """
        with self._lock:
            if self.running:
                self.elapsed_time += time.time() - self.start_time
            self.running = False

        # Wait for display thread to finish
        if hasattr(self, "_thread"):
            self._thread.join()
        
        # Clear timer from screen
        self._clear_timer_line()

    def pause(self):
        """
        Pause the stopwatch, but we can resume later.
        We'll stop the display thread, store the partial time,
        and also clear the timer from the screen.
        """
        with self._lock:
            if self.running:
                self.elapsed_time += time.time() - self.start_time
                self.running = False

        # Wait for display thread to finish
        if hasattr(self, "_thread"):
            self._thread.join()

        # Clear the timer line
        self._clear_timer_line()

    def resume(self):
        """
        Resume from a pause - do NOT reset the elapsed_time,
        but do launch the thread again to display.
        """
        with self._lock:
            if not self.running:
                # So we add any new time to elapsed_time
                # (i.e. we do NOT reset elapsed_time)
                self.start_time = time.time()
                self.running = True

        self._thread = threading.Thread(target=self.display, daemon=True)
        self._thread.start()

    # def get_elapsed_time(self):
    #     """
    #     Return the total time. If running, includes time since last resume.
    #     """
    #     with self._lock:
    #         if self.running:
    #             return self.elapsed_time + (time.time() - self.start_time)
    #         else:
    #             return self.elapsed_time

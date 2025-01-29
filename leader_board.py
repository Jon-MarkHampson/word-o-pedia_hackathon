import os
import json
import config

class Leaderboard:
    def __init__(self, filename="leaderboard.json"):
        """
        Initialise the leaderboard in a json file for persistence.
        Creates the file if it does not exist and loads existing data if t does
        """
        self.filename = filename
        self.leaderboard = self._load_leaderboard()

    def _load_leaderboard(self):
        """
        Load the leaderboard data from JSON file.
        Returns an empty dict if the file does not exist or is invalid,
        Such that we always have a dict to work with, if starting fresh or loading existing scores
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"\n{config.Fore.RED}Warning: Leaderboard file is corrupted. Starting with empty leaderboard.{config.Style.RESET_ALL}")
                return {}
        return {}

    def _save_leaderboard(self):
        """
        Save the current leaderboard data to the JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.leaderboard, file, indent=2)
        except Exception as e:
            print(f"\n{config.Fore.RED}Error saving leaderboard: {str(e)}{config.Style.RESET_ALL}")

    def update_leaderboard(self, name, difficulty, final_time):
        """
        Updates leaderboard with a new entry or replaces an existing one.
        Auto saves changes to the file.
        """
        # Init the difficulty if not already in the leaderboard
        if difficulty not in self.leaderboard:
            self.leaderboard[difficulty] = []

        # Check if the name already exists in the difficulty
        for entry in self.leaderboard[difficulty]:
            if entry["name"] == name:
                old_time = entry["time"]  # Store previous time for comparison
                old_minutes, old_seconds = divmod(old_time, 60)
                new_minutes, new_seconds = divmod(final_time, 60)

                # Update the score if the new time is better
                if final_time < old_time:
                    entry["time"] = final_time
                    print(
                        f"\n{config.Fore.GREEN}Updated {name}'s score for {difficulty} "
                        f"from {int(old_minutes):02d}:{int(old_seconds):02d} to "
                        f"{int(new_minutes):02d}:{int(new_seconds):02d}!{config.Style.RESET_ALL}")

                    # Sort before save
                    self.leaderboard[difficulty].sort(key=lambda x: x["time"])
                    self._save_leaderboard()  # Save only when updating
                else:
                    print(
                        f"\n{config.Fore.YELLOW}{name} already has a better time for {difficulty}: "
                        f"{int(old_minutes):02d}:{int(old_seconds):02d}{config.Style.RESET_ALL}")
                return  # Exit early, since we found the player

        # Add a new entry if the name is not found
        self.leaderboard[difficulty].append({
            "name": name,
            "time": final_time
        })
        new_minutes, new_seconds = divmod(final_time, 60)
        print(
            f"\n{config.Fore.CYAN}Added {name} to the leaderboard for {difficulty} "
            f"with {int(new_minutes):02d}:{int(new_seconds):02d}{config.Style.RESET_ALL}")

        # Sort before save
        self.leaderboard[difficulty].sort(key=lambda x: x["time"])
        self._save_leaderboard()

    def display_leaderboard(self):
        """
        Displays the leaderboard in a readable format.
        """
        if not self.leaderboard:
            print(f"\n{config.Fore.YELLOW}No leaderboard data available yet.{config.Style.RESET_ALL}\n")
            return

        print(f"\n{config.Fore.CYAN}=== LEADERBOARD ==={config.Style.RESET_ALL}")
        for difficulty, scores in self.leaderboard.items():
            print(f"\n{config.Fore.GREEN}Difficulty: {difficulty}{config.Style.RESET_ALL}")
            for rank, entry in enumerate(scores, start=1):
                minutes, seconds = divmod(entry["time"], 60)
                # Color code the ranks: Gold for 1st, Silver for 2nd, Bronze for 3rd, default for others
                rank_color = config.Fore.LIGHTYELLOW_EX if rank == 1 else \
                    config.Fore.WHITE if rank == 2 else \
                        config.Fore.YELLOW if rank == 3 else \
                            config.Fore.BLUE

                print(
                    f"  {rank_color}{rank}. {entry['name']} - {int(minutes):02d}:{int(seconds):02d}{config.Style.RESET_ALL}")
        print("\n")

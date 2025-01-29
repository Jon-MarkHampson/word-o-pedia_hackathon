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
                print("\nWarning: Leaderboard file is corrupted. Starting with empty leaderboard")
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
            print(f"\nError saving leaderboard: {str(e)}")

    def update_leaderboard(self, name, difficulty, final_time):
        """
        Updates leaderboard with a new entry or replaces an existing one
        Auto saves changes to the file
        """
        # Init the difficulty if not already in the leaderboard
        if difficulty not in self.leaderboard:
            self.leaderboard[difficulty] = []

        # Check if the name already exists in the difficulty
        for entry in self.leaderboard[difficulty]:
            if entry["name"] == name:
                # Update the score if the new time is better
                if final_time < entry["time"]:
                    entry["time"] = final_time
                    print(f"\nUpdated {name}'s score for {difficulty} to {final_time} seconds!")
                else:
                    print(f"\n{name} already has a better time for {difficulty}: {entry['time']} seconds.")
                break
        else:
            # Add a new entry if the name is not found
            self.leaderboard[difficulty].append({
                "name": name,
                "time": final_time
            })
            print(f"\nAdded {name} to the leaderboard for {difficulty} with {final_time} seconds.")

            # Save changes to file
            self._save_leaderboard()

    def display_leaderboard(self):
        """
        Displays the leaderboard in a readable format.
        """
        if not self.leaderboard:
            print("\nNo leaderboard data available yet.\n")
            return

        print("\n--- Leaderboard ---")
        for difficulty, scores in self.leaderboard.items():
            print(f"\nDifficulty: {difficulty}")
            for rank, entry in enumerate(scores, start=1):
                print(f"  {rank}. {entry['name']} - {entry['time']} seconds")
        print("\n")

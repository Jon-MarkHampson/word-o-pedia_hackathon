leaderboard = {}

def update_leaderboard(name, difficulty, final_time):
    """
    Updates the in-memory leaderboard with a new entry or replaces an existing one.
    """
    # Initialize the difficulty if not already in the leaderboard
    if difficulty not in leaderboard:
        leaderboard[difficulty] = []

    # Check if the name already exists in the difficulty
    for entry in leaderboard[difficulty]:
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
        leaderboard[difficulty].append({
            "name": name,
            "time": final_time
        })
        print(f"\nAdded {name} to the leaderboard for {difficulty} with {final_time} seconds.")

    # Sort the leaderboard for the difficulty by time
    leaderboard[difficulty].sort(key=lambda x: x["time"])


def display_leaderboard():
    """
    Displays the in-memory leaderboard in a readable format.
    """
    if not leaderboard:
        print("\nNo leaderboard data available yet.\n")
        return

    print("\n--- Leaderboard ---")
    for difficulty, scores in leaderboard.items():
        print(f"\ndifficulty: {difficulty}")
        for rank, entry in enumerate(scores, start=1):
            print(f"  {rank}. {entry['name']} - {entry['time']} seconds")
    print("\n")
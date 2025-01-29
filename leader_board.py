leaderboard = {}

def update_leaderboard(name, level, passed_time):
    """
    Updates the in-memory leaderboard with a new entry or replaces an existing one.
    """
    # Initialize the level if not already in the leaderboard
    if level not in leaderboard:
        leaderboard[level] = []

    # Check if the name already exists in the level
    for entry in leaderboard[level]:
        if entry["name"] == name:
            # Update the score if the new time is better
            if passed_time < entry["time"]:
                entry["time"] = passed_time
                print(f"\nUpdated {name}'s score for {level} to {passed_time} seconds!")
            else:
                print(f"\n{name} already has a better time for {level}: {entry['time']} seconds.")
            break
    else:
        # Add a new entry if the name is not found
        leaderboard[level].append({
            "name": name,
            "time": passed_time
        })
        print(f"\nAdded {name} to the leaderboard for {level} with {passed_time} seconds.")

    # Sort the leaderboard for the level by time
    leaderboard[level].sort(key=lambda x: x["time"])


def display_leaderboard():
    """
    Displays the in-memory leaderboard in a readable format.
    """
    if not leaderboard:
        print("\nNo leaderboard data available yet.\n")
        return

    print("\n--- Leaderboard ---")
    for level, scores in leaderboard.items():
        print(f"\nLevel: {level}")
        for rank, entry in enumerate(scores, start=1):
            print(f"  {rank}. {entry['name']} - {entry['time']} seconds")
    print("\n")
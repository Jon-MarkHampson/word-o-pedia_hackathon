"""
Funcitons for getting and filtering words from Wikipedia
"""
import config
import re
import wikipediaapi
import random

def get_game_topic():
    while True:
        # Prompt user for choice
        choice = input("\nWould you like a random topic or to type your own? (R for Random, T for Topic): ").strip().lower()
        if choice not in {"r", "t"}:
            print("\nInvalid choice. Please enter 'R' for Random or 'T' for Topic.")
            continue

        if choice == "r":
            # Random topic selection
            random_topics = ["Space Exploration", "Artificial Intelligence", "Music", "Quantum Physics", "Olympic Sports", "Snakes", "Guido van Rossum", "Monty Python"] # Changed "Music Genres" to "Music" ADD MORE TOPICS
            page_title = random.choice(random_topics)
            print(f"\nRandomly selected topic: {page_title}\n")
            return page_title
        else:
            # Prompt user to type in a topic
            return input("Type in a topic for the word search (e.g., 'Space Exploration'): ").strip().lower()
   

def get_links_from_wiki(user_input="Nelson Mandela"):
    """Fetches and returns a list of titles of links from a Wikipedia page."""
    wiki_api = wikipediaapi.Wikipedia(language=config.WIKI_LANGUAGE, user_agent="word-o-pedia/v1")
    page = wiki_api.page(user_input)

    if not page.exists():
        print(f"Error: Page '{user_input}' does not exist.")
        return []

    return list(page.links.keys())


def filter_game_words(links, grid_size, num_words):
    """
    Filters the Wikipedia links to include only valid words
    and selects words evenly across the list.
    """
    valid_links = [link.lower() for link in links if re.match(r"^[A-Za-z]+$", link) and len(link) <= grid_size]
    if not valid_links:
        print("No valid words found on the Wikipedia page!")
        return []
    
    step = max(1, len(valid_links) // num_words)  # Ensure step is at least 1
    randomise_list_start = random.randint(0, step - 2)  # Randomise the starting point
    # print(f"DEBUG Randomised list start: {randomise_list_start}")
    return valid_links[randomise_list_start::step][:num_words]


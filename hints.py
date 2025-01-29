import os
import openai
import wikipediaapi
import textwrap
import config
import mask_word

from dotenv import load_dotenv


def get_api_key():
    # 1) Load environment variables
    load_dotenv()

    # 2) Set the OpenAI API key
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Optional: Raise an error if key is missing
    if not openai.api_key:
        raise ValueError("API key not found. Ensure OPENAI_API_KEY is set in your .env file.")
    
    return openai.api_key


def get_hint_about_word(word):
    """
    Generate a hint (brief summary) using OpenAI's new chat interface,
    and reveal letters of the first word incrementally based on hint_counter.

    - If the GPT summary is only one word, we partially reveal that single word.
    - If the GPT summary has multiple words, we partially reveal the first one,
      then keep the rest unchanged.

    Returned tuple: (length_of_first_word, wrapped_output)
    """
    get_api_key()
    
    wiki_api = wikipediaapi.Wikipedia(language=f"{config.WIKI_LANGUAGE}", user_agent="word-o-pedia/v1")
    page = wiki_api.page(word)

    if not page.exists():
        return f"Sorry, no information found for the word: {word}"

    input_string = page.summary

    while True:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant that summarizes a topic concisely."
                    },
                    {
                        "role": "user",
                        "content": f"Summarize this text in one sentence: {input_string}. The response must start with the word {word}. Never put punctuation after the word {word}.",
                        "temperature": 0.1
                    }
                ],
            )

            # Grab the summary text
            chat_gtp_summary = response.choices[0].message.content.strip()
            
            # Split summary at first_word
            word_check = chat_gtp_summary.split(" ", 1)[0].lower()
            hint = chat_gtp_summary.split(" ", 1)[1] if " " in chat_gtp_summary else ""
            word = word.lower()
            
            if word_check == word:
              
                # Wrap text to 50 chars
                wrapped_hint = textwrap.fill(hint, width=70)
                masked_summary = mask_word.mask_word_in_text(wrapped_hint, word)

                return masked_summary
                    
        except Exception as e:
            return f"Sorry, couldn't generate a hint for the word because: {str(e)}"


def reveal_the_word(word, hint_counter):

            # The portion to reveal (characters up to hint_counter)
            revealed_part = word[:hint_counter].upper()

            # The portion to hide (the rest of the letters)
            to_hide_length = max(0, len(word) - hint_counter)

            # Turn revealed letters into a spaced string: "M A N G O"
            revealed_part_spaced = " ".join(revealed_part)

            # Turn the hidden letters into spaced stars: "* * *"
            hidden_part_spaced = " ".join(["*"] * to_hide_length)

            # Combine them
            combined_word = revealed_part_spaced
            if revealed_part_spaced and hidden_part_spaced:
                # space between revealed and hidden
                combined_word += " "  
            combined_word += hidden_part_spaced

            # Return the combined revealed word
            return combined_word


def create_summary_for_how_word_relates_to_topic(word, topic):
    """
    Generate a summary about the topic using OpenAI's new chat interface.
    """
    get_api_key()

    while True:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant that summarizes the relation of a keyword to a topic very concisely."
                    },
                    {
                        "role": "user",
                        "content": f"Summarize how {word} relates to {topic} in a few sentences.",
                        "temperature": 0.1
                    }
                ],
            )

            # Grab the summary text
            chat_gtp_summary = response.choices[0].message.content.strip()

            return chat_gtp_summary
        except Exception as e:
            return f"Sorry, couldn't generate a summary for the keyword because: {str(e)}"


def generate_summaries_for_all_game_words(game_words, topic):
    """
    Generate a summary for each game word in the list.
    """

    summaries = {}
    for word in game_words:
        word = word.upper()
        summaries[word] = create_summary_for_how_word_relates_to_topic(word, topic)
    return summaries


def print_summaries(summaries):
    """
    Print the summaries in a formatted way.
    """
    if not isinstance(summaries, dict):
        raise TypeError(f"Expected a dictionary, but got {type(summaries).__name__}")

    if not summaries:
        print("No summaries available.")
        return

    for i, (word, summary) in enumerate(summaries.items()):
        wrapped_summary = textwrap.fill(summary, width=70)
        print(f"\n{config.COLOURS_LIST[i % len(config.COLOURS_LIST)]}{word}{config.Style.RESET_ALL}:\n{wrapped_summary}\n")

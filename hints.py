import os
import openai
import wikipediaapi
import textwrap
import config

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


def get_hint_about_word(word, hint_counter):
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

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant that summarizes text very briefly."
                },
                {
                    "role": "user",
                    "content": f"Summarize this text in one sentence: {input_string}. The response must start with the word {word}. Never put puctuation after the word {word}."
                }
            ],
        )

        # Grab the summary text
        summary = response.choices[0].message.content.strip()
        
        # print("DEBUG: ", summary)

        # Split summary at first_word

        hint = summary.split(" ", 1)[1] if " " in summary else ""

        # print("DEBUG: ", hint)
        
        # Wrap text to 50 chars
        wrapped_hint = textwrap.fill(hint, width=50)
        # print("DEBUG wrapped: ", wrapped_hint)
        return wrapped_hint
    
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
                combined_word += " "  # space between revealed and hidden
            combined_word += hidden_part_spaced


            # Return the combined revealed word
            return combined_word



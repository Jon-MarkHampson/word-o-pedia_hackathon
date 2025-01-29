
import re

def mask_word_in_text(text, word):
    """
    Replace all case-insensitive occurrences of a word in text with asterisks.
    
    Args:
        text (str): The text to search through
        word (str): The word to mask
        
    Returns:
        str: Text with the word replaced by asterisks
    """
    
    # Create a pattern that matches the word with word boundaries
    # (?i) makes it case insensitive
    # \b adds word boundaries to prevent matching parts of other words
    pattern = fr'(?i)\b{re.escape(word)}\b'
    
    # Replace the word with asterisks of the same length
    return re.sub(pattern, lambda m: '*' * len(m.group()), text)

# Example usage:
# chat_gpt_summary = "The player should look for the word elephant hidden in the puzzle."
# word_to_find = "elephant"
# masked_hint = mask_word_in_text(chat_gpt_summary, word_to_find)
# print(masked_hint)
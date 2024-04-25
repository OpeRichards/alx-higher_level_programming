#!/usr/bin/python3
"""This module defines a function ``text_indentation``."""


def text_indentation(text):
    """Prints text with 2 new lines after each `.`, `?` or `:` charcters.
    Args:
        text (str): Input to break into separate lines.
    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize starting index of each line
    start_index = 0
    
    # Iterate through each charcter in the text
    for i, char in enumerate(text):
        # If char is `.`, `?` or `:`
        if char in ('.', '?', ':'):
            # Print text from start_index to current index
            print(text[start_index:i + 1].strip())
            # Print two new lines
            print("\n" * 2, end="")
            # Update start_index to next character index
            start_index = i + 1

    # Print remaining text if any
    if start_index < len(text):
        print(text[start_index:].strip())

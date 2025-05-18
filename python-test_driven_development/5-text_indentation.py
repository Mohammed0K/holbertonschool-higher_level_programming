#!/usr/bin/python3
"""This module defines a function a text with 2 new lines after each of these characters: ., ? and :.
    """


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace multiple spaces with a single space
    text = ' '.join(text.split())

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the text
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Print the final result without leading/trailing whitespace
    print(result.strip(), end="")

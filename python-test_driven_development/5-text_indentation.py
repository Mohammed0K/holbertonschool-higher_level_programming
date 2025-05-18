#!/usr/bin/python3
"""
5-text_indentation module
Defines a function that prints a text with two new lines
after each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints text with two new lines after each occurrence of '.', '?' or ':'.
    Arguments:
        text (str): The input text to process.
    Raises:
        TypeError: If `text` is not a string.
        ValueError: If `text` is an empty string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if text == "":
        raise ValueError("text must be a string")

    i = 0
    length = len(text)
    result = ""

    while i < length:
        ch = text[i]
        result += ch
        if ch in ".?:":
            # after punctuation, add two newlines
            result += "\n\n"
            # skip any spaces immediately following the punctuation
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    # print without adding extra newline at the end
    print(result, end="")

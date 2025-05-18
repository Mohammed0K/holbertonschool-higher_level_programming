#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :
    - .: each of these characters should be followed by 2 new lines
    - text should not be empty
    - text should be a string"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after ".?:" characters
    Args:
        text (str): The text to be printed
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    char_i = text[:]

    for df in ".?:":
        list_text = df.split(df)
        char_i = ""
        for i in list_text:
            i = i.strip(" ")
            char_i = i + df if char_i is "" else char_i + "\n\n" + i + df

    print(char_i[:-3], end="")
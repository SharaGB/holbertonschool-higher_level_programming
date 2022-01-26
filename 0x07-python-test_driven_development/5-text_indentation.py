#!/usr/bin/python3
"""
This is the ``text_indentation`` module.

The text_indentation module supplies one function, text_indentation(text)
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delimiter = 0
    while delimiter < len(text):
        if text[delimiter] == "." or text[delimiter] == "?"\
                or text[delimiter] == ":":
            text = text[:(delimiter + 1)] + "\n\n" + text[(delimiter + 1):]
        delimiter += 1
    new_text = "\n".join(string.strip() for string in text.splitlines(1))
    print(new_text, end='')

#!/usr/bin/python3
"""text conversion"""


def text_indentation(text):
    """text conversion"""
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".")
    new_text = new_text.replace("? ", "?")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace(".", ".\n\n")
    new_text = new_text.replace("?", "?\n\n")
    new_text = new_text.replace(":", ":\n\n")
    print(new_text, end='')

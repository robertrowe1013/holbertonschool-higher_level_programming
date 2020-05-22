#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".\n\n")
    new_text = new_text.replace("? ", "?\n\n")
    new_text = new_text.replace(": ", ":\n\n")
    print(new_text, end='')

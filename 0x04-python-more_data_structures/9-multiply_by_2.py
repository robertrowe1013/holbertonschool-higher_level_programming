#1/usr/bin/python39
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in a_dictionary:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary

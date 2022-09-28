#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    first_key = list(a_dictionary.keys())[0]
    first_value = a_dictionary[first_key]

    for k, v in a_dictionary.items():
        if v > first_value:
            first_value = v
            first_key = k
        return first_key

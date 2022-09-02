#!/usr/bin/python3
def best_score(a_dictionary):
    best_value = 0
    if a_dictionary == {}:
        return None
    else:
        for key, value in a_dictionary.items():
            if value > best_value:
                best_value = value
            else:
                continue
        best_key = list({i for i in a_dictionary if a_dictionary[i] == best_value})
        return best_key[0]

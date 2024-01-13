#!/usr/bin/python3
def best_score(A_dictionary):
    if not a_dictionary:
        return None
    Max = 0
    for k, value in a_dictionary.items():
        if value > Max:
            Max = value
            for key, value in a_dictionary.items():
                if value == Max:
                    return key

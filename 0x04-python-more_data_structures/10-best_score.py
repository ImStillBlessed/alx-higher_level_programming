#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = max(a_dictionary, key=a_dictionary.get)
    return {biggest: a_dictionary[biggest]}

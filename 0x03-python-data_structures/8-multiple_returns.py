#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first = None
        length = 0
    else:
        length = len(sentence)
        for ch in sentence:
            first = ch
            break
    return length, first

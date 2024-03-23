#!/usr/bin/python3
def multiple_returns(sentence):
    for xrs in sentence:
        length = len(sentence)
        first_xr = sentence[0]
        if sentence == '':
            return None
        else:
            return (length, first_xr)

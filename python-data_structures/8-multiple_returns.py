#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        infos = len(sentence), None
        return (infos)
    else:
        infos = len(sentence), sentence[0]
        return (infos)

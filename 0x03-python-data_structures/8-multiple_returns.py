#!/usr/bin/python3
#multiple_returns - Returns len of str and first character

def multiple_returns(sentence):
    if sentence == '':
        return 0, None
    else:
        return len(sentence), sentence[0]

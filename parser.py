# -*- coding: latin-1 -*-

import re


def parse(string):
    if ' / ' or ',' in string:                      # Acts SEEM to MOSTLY be split on a forward slash or a comma
        acts = re.split('\s/\s|,', string)          # split on ' / ' or ','
        for act in acts:
            string = stripper(act.strip())
    else:
        string = stripper(string)

    string = string.strip() + "\n"
    return string.encode('utf-8')


def stripper(string):
    # while gross, the performance matters so little - this will do for now
    string = string.replace("\t", "")       # remove those nasty tabs
    string = string.replace("\n", "")       # newlines
    string = string.replace(",", "")        # commas
    string = string.replace("  ", "")       # double spaces
    string = string.replace(":", "")        # colons
    string = string.replace("(", "")        # left bracket
    string = string.replace(")", "")        # right bracket
    string = string.replace("-", "")        # hyphens

    # must be a better syntax
    if 'sold out' in string:
        string = string.replace('sold out', '')
    if 'cancelled' in string:
        string = string.replace('cancelled', '')
    if 'selling fast' in string:
        string = string.replace('selling fast', '')
    if 'last few' in string:
        string = string.replace('last few', '')
    if 'early bird' in string:
        string = string.replace('early bird', '')
    if 'date change' in string:
        string = string.replace('date change', '')
    if 'seated' in string:
        string = string.replace('seated', '')

    # sketchy
    if 'new' in string:
        string = string.replace('new', '')

    return string + "\n"

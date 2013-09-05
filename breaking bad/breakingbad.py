#!/usr/bin/env python
import sys

ANSI_DEFAULT = '\033[0m'
ANSI_HIGHLIGHT = '\033[32m'

elements = [
    'ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', 'b', 'ba', 'be', 'bh', 'bi','bk', 'br', 'c',
    'ca', 'cd', 'ce', 'cf', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'db', 'ds', 'dy', 'er', 'es',
    'eu', 'f', 'fe', 'fl', 'fm', 'fr', 'ga', 'gd', 'ge', 'h', 'he', 'hf', 'hg', 'ho', 'hs', 'i',
    'in', 'ir', 'k', 'kr', 'la', 'li', 'lr', 'lu', 'lv', 'md', 'mg', 'mn', 'mo', 'mt', 'n', 'na',
    'nb', 'nd', 'ne', 'ni', 'no', 'np', 'o', 'os', 'p', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt',
    'pu', 'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', 's', 'sb', 'sc', 'se', 'sg', 'si', 'sm',
    'sn', 'sr', 'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', 'u', 'uuo', 'uup', 'uus', 'uut',
    'v', 'w', 'xe', 'y', 'yb', 'zn', 'zr',
]

def longest_substring_position_in_string(string, substrings):
    for element in sorted(elements, key=lambda x: len(x), reverse=True):
        if element in string:
            start = string.index(element)
            end = start + len(element)
            return (start, end)

def highlight_string(string, start, end):
    highlighted_string = "".join([
        string[:start],
        ANSI_HIGHLIGHT,
        string[start:end],
        ANSI_DEFAULT,
        string[end:]
    ])

    return highlighted_string

if __name__ == '__main__':

    words = sys.argv[1]

    strings = []

    for word in words.split(' '):
        symbol_range = longest_substring_position_in_string(word, elements)
        if symbol_range:
            start, end = symbol_range
            word = highlight_string(word, start, end)

        strings.append(word)

    print " ".join(strings)
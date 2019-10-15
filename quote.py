"""
A python file handling some quotes
"""

import random

lunchBTH = [
    'thairestaurangen vid korsningen?',
    'det är lite mysigt i fiket jämte demolabbet?',
    'Indiska?',
    'Pappa curry?',
    'boden uppe på parkeringen?',
    'Bergåsa kebab?',
    'Pasterian?',
    'Villa Oscar?',
    'Eat here?',
    'Bistro J?'
]

feelings = [
    'I\'m feeling really happy today =)',
    'Today\'s not one of my better days.',
    'I\'m not feeling good nor bad.',
    'The sun is shining, so how can\'t you feel good?',
    'HOW DO YOU THINK I FEEL BEING A ROBOT?!'
]

fav_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

float_number = [1.124, 2.325, 6.234, 7.523, 1.425, 9.575, 10.234, 13.245, 4.234]

def read_citation():
    """
    Reads a citation
    """
    f = open("quotes.txt", "r")
    _number = random.randint(1, 10)
    spec_line = f.readlines()
    return spec_line[_number]


def read_lunch():
    """
    Prints out random lunch restaurant
    """
    f = open("lunch.txt", "r")
    _number = random.randint(5, 19)
    spec_line = f.readlines()
    return spec_line[_number]

def read_hej():
    """
    Reads a random hello message
    """
    f = open("lunch.txt", "r")
    _number = random.randint(0, 3)
    spec_line = f.readlines()
    return spec_line[_number]

def read_mat():
    """
    Reads other restaurants from an array in this file (instead from text file)
    """
    return lunchBTH[random.randint(0, 9)]

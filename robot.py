"""
A program where you can get help by a robot
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def menu():
    '''
    prints menu
    '''
    print("2) Farenheit to Celsius")
    print("3) Multiply words")
    print("4) Sum and mean value")
    print("5) Which number is bigger?")
    print("6) Prolong word")
    print("7) Isogram")
    print("8) Word Shaker")
    print("9) Anagram")
    print("10) Acronym Generator")
    print("11) Hide a word")
    print("q) Quit.")

def celcius_convert():
    '''
    prints greeting
    '''
    celsius = input("Temperature in celsius you want to convert to farenheit? ")
    farenheit = int(celsius) * 9 / 5 + 32
    print(str(farenheit))
    print()
    print("Thank you, that's all for today")

def word_multiplicator():
    '''
    multiplies a word
    '''
    word = input("please say a word ")
    number = input("now a number ")
    print(str(word + " ") * int(number))

def sum_and_mean():
    '''
    prints out sum and mean of numbers
    '''
    number = list(map(int, input("Enter a multiple value: ").split()))
    summa = sum(number)
    median = summa / len(number)
    _round = round(median, 1)
    print("the sum of all values is ", summa)
    print("the mean value of the numbers is ", _round)

def which_is_bigger():
    '''
    tells u which number is the biggest
    '''
    number1 = input("Enter a number: ")
    number2 = input("Give me another number: ")
    if number1 == "done" or number2 == "done":
        print("You want to stop? ")
    else:
        while number1 != "done" or number2 != "done":
            if number1 > number2:
                print("your last number was smaller")
                number1 = input("Enter a number: ")
                number2 = input("Give me another number: ")
                if number1 == "done" or number2 == "done":
                    break
            elif number1 == number2:
                if number1 == "done" or number2 == "done":
                    break
                print("the numbers are equal")
                number1 = input("Enter a number: ")
                number2 = input("Give me another number: ")
            else:
                if number1 == "done" or number2 == "done":
                    break
                print("your last number was bigger")
                number1 = input("Enter a number: ")
                number2 = input("Give me another number: ")

def prolong_word():
    '''
    makes you word increase by every letter
    '''
    string = input("Enter a string: ")
    string2 = [k for k in string]
    new_word = ''
    j = 1
    i = 0

    while i < len(string2):
        new_word += string2[0]
        i += 1
        while j < len(string2):
            new_word += string2[j] * j + "-"
            j += 1
            print(new_word)

def isogram_checker():
    '''
    checks if word is isogram or not
    '''
    isogram = input("Enter a word ")
    control = [k for k in isogram]
    word_array = []
    # print(control)
    is_isogram = True

    for letter in control:
        if letter in word_array:
            is_isogram = False
        else:
            word_array.append(letter)
    print("Is the word " + str(isogram) + " an isogram? \n " + "The answer is: " + str(is_isogram))

def word_shaker():
    '''
    shakes up a word
    '''
    word = input("Please just give me a word: ")
    shaker = ''.join(random.choice(word) for i in range(len(word)))
    print(shaker)

def anagram():
    '''
    tells u if a word is an anagram
    '''
    word1 = input("Give me a first word: ")
    word2 = input("Now give me a second word: ")
    if (sorted(word1) == sorted(word2)):
        print("We have an anagram here!")
    else:
        print("No anagram :(")

def acronym():
    '''
    turns a word into an acronym
    '''
    word = input("Give me a word I turn into an acronym: ")
    acro = ""
    for char in word:
        if char.isupper():
            acro += char
    print(acro)

def censur():
    '''
    prints "#" for all chars in word except last 4
    '''
    word = input("Give me a word to censur (has to be at least 5 chars long): ")
    censur1 = word[-4:]
    new_censur = ""
    i = 0
    while i < len(word) - 4:
        new_censur += "#"
        i += 1
    new_censur += censur1
    print(new_censur)

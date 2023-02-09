'''
CMPT120 LAB 4 
    This is a lab assignment with the focus on practicing funtions

Author: Tristan Barboni - 
Date: 2/9/2023
'''
from string import ascii_lowercase as alphabet

# This first funtion is supposed to conacatonate multiple strings from a list.
def join_strings(strings):
    return "".join(strings)

#This fucnition will take three parameters and fill them in the blanks of a MADLib
def mad_libs(name, noun, event):
    return f"{name} is too cool for {noun} class. Instead she/he will be attending the {event}"


#This function will act as a Caesar Cipher encoder and decoder
def caesar_cipher(text, shift):
    result = ""
    cipher_lookup = {char: alphabet[(i + shift) % 26] for i, char in enumerate(alphabet)}
    for i in text.lower():
        result += cipher_lookup.get(i, i)
    return result


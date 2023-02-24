'''
Assignment #5:

    Tests the various capabilities of the functions  
    defined in the conditionals.py file.


@author Kevin Hayden
@date 2023-02-11
@org Marist College - Department of Computing Science

Syntax for single decision:

if <condition> :
    <body>
    
Syntax for 2-way decision:

if <condition> :
    <body>
else:
    <body>

Syntax for Multi-way decision:

if <condition> :
    <body>
elif <condition> :
    <body>
else:
    <body>
    
Syntax for try/catch:

try:
    <body>
except <exception-type> :
    <body>
'''
# This is a funtion to test three parameters and check to see if they are equilaterals


from statistics import mean


def is_equilateral(x, y, z):
    if type(x) is not int:
        raise TypeError("Only integers are allowed")
    elif type(z) is not int:
        raise TypeError("Only integers are allowed")
    elif type(y) is not int:
        raise TypeError("Only integers are allowed")
    else:
        if x == y and y == z:
            return True
        else:
            return False

#This is a function designed to pick out the vowels from a text input
def get_vowels(text):
    if type(text) is not str:
        raise TypeError("Only strings are allowed")
    else:
        vowels = []
        for vowel in text:
            if vowel.lower() == ("a"):
                vowels.append(vowel)
            elif vowel.lower() == ("e"):
                vowels.append(vowel)
            elif vowel.lower() == ("i"):
                vowels.append(vowel)
            elif vowel.lower() == ("o"):
                vowels.append(vowel)
            elif vowel.lower() == ("u"):
                vowels.append(vowel)
        return vowels

#This is a function used later to validate that a list of grades is appropriate
def validate_list(grades):
    if type(grades) is not list:
        raise TypeError("Grades must be a list")
    elif grades == []:
        raise Exception("List must not be empty")
    for i in grades:
        if type(i) != int:
            raise Exception("Elements in list must be integers")
        if 0 > i or i > 100:
            raise Exception("Grades must be between 0 nad 100")
    else:
        return grades

#This is a function designed to check if a given string is a palindrome
def is_palindrome(text):
    if type(text) != str:
        raise TypeError("Text must be a string")

    half = len(text) // 2
    for i in range(0, half):
        if (text.lower()[i] != text.lower()[len(text) - i - 1]):
            return False
    return True

#This is a function to convert the average grade into a letter grade.
def calculate_letter_grade(grades):
    validate_list(grades)
    grade_avg = mean(grades)
    if grade_avg >= 93:
        return "A"
    elif grade_avg >= 90:
        return "A-"
    elif grade_avg >= 87:
        return "B+"
    elif grade_avg >= 83:
        return "B"
    elif grade_avg >= 80:
        return "B-"
    elif grade_avg >= 77:
        return "C+"
    elif grade_avg >= 73:
        return "C"
    elif grade_avg >= 70:
        return "C-"
    elif grade_avg >= 67:
        return "D+"
    elif grade_avg >= 63:
        return "D"
    elif grade_avg >= 60:
        return "D-"
    else:
        return "F"

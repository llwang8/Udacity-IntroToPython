# Udacity
# Intro to Python

# Lesson 4: Files and Modules

# Tuples

def hours2days(hours):
    return (int(hours/24), hours % 24)

print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))

# Default Arguments
def print_list(l, numbered=True, bullet_character='-'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))


# Reading from a file
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt') as f:
    #use the for loop syntax to process each line
        for line in f:
    #and add the actor name to cast_list
            cast_list.append(line.strip().split(',')[0])

    return cast_list


# TODO: print e to the power of 3 using the math module
import math
print(math.exp(3))



# Your function should return a string consisting of three random
# words concatenated together without spaces
# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

def generate_password():
    strlist = []
    for i in range(3):
        index = random.randint(0, len(word_list))
        strlist.append(word_list[index])
    return ''.join(strlist)

def generate_password1():
    return str().join(random.sample(word_list, 3))

print(generate_password())


# Third-Party Libraries

from datetime import datetime

import pytz

utc = pytz.utc # utc is Coordinated Universal Time
ist = pytz.timezone('Asia/Kolkata') #IST is Indian Standard Time

now = datetime.datetime.now(tz=utc) # this is the current time in UTC
ist_now = now.astimezone(ist) # this is the current time in IST.




